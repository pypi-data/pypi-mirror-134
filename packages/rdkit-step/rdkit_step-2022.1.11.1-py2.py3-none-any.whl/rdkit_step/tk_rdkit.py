# -*- coding: utf-8 -*-

"""The graphical part of a RDKit step"""

import pprint  # noqa: F401
import tkinter as tk
import tkinter.ttk as ttk

import rdkit_step  # noqa: F401
import seamm
from seamm_util import ureg, Q_, units_class  # noqa: F401
import seamm_widgets as sw
import Pmw


class TkRdkit(seamm.TkNode):
    """
    The graphical part of a RDKit step in a flowchart.

    Attributes
    ----------
    tk_flowchart : TkFlowchart = None
        The flowchart that we belong to.
    node : Node = None
        The corresponding node of the non-graphical flowchart
    namespace : str
        The namespace of the current step.
    tk_subflowchart : TkFlowchart
        A graphical Flowchart representing a subflowchart
    canvas: tkCanvas = None
        The Tk Canvas to draw on
    dialog : Dialog
        The Pmw dialog object
    x : int = None
        The x-coordinate of the center of the picture of the node
    y : int = None
        The y-coordinate of the center of the picture of the node
    w : int = 200
        The width in pixels of the picture of the node
    h : int = 50
        The height in pixels of the picture of the node
    self[widget] : dict
        A dictionary of tk widgets built using the information
        contained in RDKit_parameters.py

    See Also
    --------
    Rdkit, TkRdkit,
    RdkitParameters,
    """

    def __init__(
        self,
        tk_flowchart=None,
        node=None,
        canvas=None,
        x=None,
        y=None,
        w=200,
        h=50,
    ):
        """
        Initialize a graphical node.

        Parameters
        ----------
        tk_flowchart: Tk_Flowchart
            The graphical flowchart that we are in.
        node: Node
            The non-graphical node for this step.
        namespace: str
            The stevedore namespace for finding sub-nodes.
        canvas: Canvas
           The Tk canvas to draw on.
        x: float
            The x position of the nodes center on the canvas.
        y: float
            The y position of the nodes cetner on the canvas.
        w: float
            The nodes graphical width, in pixels.
        h: float
            The nodes graphical height, in pixels.

        Returns
        -------
        None
        """
        self.dialog = None
        self.tree_state = None

        super().__init__(
            tk_flowchart=tk_flowchart,
            node=node,
            canvas=canvas,
            x=x,
            y=y,
            w=w,
            h=h,
        )

    def load_dict(self, tree, parent, metadata):
        """Custom code to load the dictionary in the test.
        NB. the 'state=False' argument prevents insert from working out the
        state of the parent nodes every time an item is inserted. This is done
        at the end with 'tree.state()'
        """
        for key, value in metadata.items():
            # Get any data in the columns
            tree.insert(
                parent,
                "end",
                iid=key,
                text=key,
                state=False,
                open="open" in value and value["open"],
                values=[value["description"] if "description" in value else ""],
            )
            # Recurse if a branch node
            if "name" not in value:
                self.load_dict(tree, key, value)

        # Set the state of intermediate nodes
        tree.state()

    def create_dialog(self, title="Specify the RDKit featurizers"):
        """Create the dialog!"""

        self.logger.debug("Creating the dialog")

        self.dialog = Pmw.Dialog(
            self.toplevel,
            buttons=("OK", "Reset", "Clear", "Cancel"),
            master=self.toplevel,
            title=title,
            command=self.handle_dialog,
        )
        self.dialog.withdraw()

        frame = ttk.Frame(self.dialog.interior())
        frame.pack(expand=tk.YES, fill=tk.BOTH)
        self["frame"] = frame

        # Create all the widgets
        P = self.node.parameters

        for key in P:
            if key not in ("results", "extra keywords", "create tables", "tree"):
                self[key] = P[key].widget(frame)

        tree = self["tree"] = sw.CheckTree(frame, columns=["Descriptions"])
        tree.heading("#0", text="Features")

        for widget in ("where",):
            w = self[widget]
            w.bind("<<ComboboxSelected>>", self.reset_dialog)
            w.bind("<Return>", self.reset_dialog)
            w.bind("<FocusOut>", self.reset_dialog)

        self.load_dict(tree, "", rdkit_step.properties)

        self["tree"].selection_set(P["features"].value)

        self.reset_dialog()

        self.logger.debug("Finished creating the dialog")

    def reset_dialog(self, widget=None):
        """Resets the dialog to the its last state"""
        frame = self["frame"]
        for slave in frame.grid_slaves():
            slave.grid_forget()

        where = self["where"].get()

        row = 0
        self["tree"].grid(row=row, column=0, columnspan=3, sticky="nesw")
        row += 1
        self["where"].grid(row=row, column=0, columnspan=2, sticky="ew")
        row += 1

        if where in ("Table", "Both"):
            self["table"].grid(row=row, column=1, sticky="ew")

        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, minsize=50)
        frame.columnconfigure(2, weight=1)

        return

    def right_click(self, event):
        """
        Handles the right click event on the node.

        Parameters
        ----------
        event : Tk Event

        Returns
        -------
        None

        See Also
        --------
        TkRdkit.edit
        """

        super().right_click(event)
        self.popup_menu.add_command(label="Edit..", command=self.edit)

        self.popup_menu.tk_popup(event.x_root, event.y_root, 0)

    def edit(self):
        """Present a dialog for editing the RDKit input

        Parameters
        ----------
        None

        Returns
        -------
        None

        See Also
        --------
        TkRdkit.right_click
        """

        if self.dialog is None:
            self.create_dialog()

        self.tree_state = self["tree"].get()

        self.dialog.activate(geometry="centerscreenfirst")

    def handle_dialog(self, result):
        """Handle the closing of the edit dialog

        What to do depends on the button used to close the dialog. If
        the user closes it by clicking the "x" of the dialog window,
        None is returned, which we take as equivalent to cancel.

        Parameters
        ----------
        result : None or str
            The value of this variable depends on what the button
            the user clicked.

        Returns
        -------
        None
        """
        if result == "Help":
            # display help!!!
            return
        elif result == "Reset":
            self["tree"].selection_set(self.tree_state)
            return
        elif result == "Clear":
            self["tree"].selection_clear("")
            return
        super().handle_dialog(result)

        P = self.node.parameters
        if result == "OK":
            P["features"].value = self["tree"].get("", as_dict=False)
        else:
            self["tree"].selection_set(self.tree_state)

    def handle_help(self):
        """Shows the help to the user when click on help button.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        print("Help not implemented yet for RDKit!")
