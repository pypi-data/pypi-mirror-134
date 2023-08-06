# -*- coding: utf-8 -*-

"""Non-graphical part of the RDKit step in a SEAMM flowchart
"""

import logging
import pprint  # noqa: F401

import numpy as np

try:
    from rdkit.Chem import Descriptors, Descriptors3D
except ModuleNotFoundError:
    print(
        "Please install rdkit using conda:\n" "     conda install -c conda-forge rdkit"
    )
    raise

import rdkit_step
from rdkit_step import metadata
import seamm
from seamm_util import ureg, Q_  # noqa: F401
import seamm_util.printing as printing
from seamm_util.printing import FormattedText as __

# In addition to the normal logger, two logger-like printing facilities are
# defined: "job" and "printer". "job" send output to the main job.out file for
# the job, and should be used very sparingly, typically to echo what this step
# will do in the initial summary of the job.
#
# "printer" sends output to the file "step.out" in this steps working
# directory, and is used for all normal output from this step.

logger = logging.getLogger(__name__)
job = printing.getPrinter()
printer = printing.getPrinter("RDKit")


class Rdkit(seamm.Node):
    """
    The non-graphical part of a RDKit step in a flowchart.

    Attributes
    ----------
    parser : configargparse.ArgParser
        The parser object.

    options : tuple
        It contains a two item tuple containing the populated namespace and the
        list of remaining argument strings.

    subflowchart : seamm.Flowchart
        A SEAMM Flowchart object that represents a subflowchart, if needed.

    parameters : RdkitParameters
        The control parameters for RDKit.

    See Also
    --------
    TkRdkit,
    Rdkit, RdkitParameters
    """

    def __init__(self, flowchart=None, title="RDKit", extension=None, logger=logger):
        """A step for RDKit in a SEAMM flowchart.

        You may wish to change the title above, which is the string displayed
        in the box representing the step in the flowchart.

        Parameters
        ----------
        flowchart: seamm.Flowchart
            The non-graphical flowchart that contains this step.

        title: str
            The name displayed in the flowchart.
        extension: None
            Not yet implemented
        logger : Logger = logger
            The logger to use and pass to parent classes

        Returns
        -------
        None
        """
        logger.debug(f"Creating RDKit {self}")

        super().__init__(
            flowchart=flowchart,
            title="RDKit",
            extension=extension,
            module=__name__,
            logger=logger,
        )  # yapf: disable

        self.parameters = rdkit_step.RdkitParameters()

    @property
    def version(self):
        """The semantic version of this module."""
        return rdkit_step.__version__

    @property
    def git_revision(self):
        """The git version of this module."""
        return rdkit_step.__git_revision__

    def description_text(self, P=None):
        """Create the text description of what this step will do.
        The dictionary of control values is passed in as P so that
        the code can test values, etc.

        Parameters
        ----------
        P: dict
            An optional dictionary of the current values of the control
            parameters.
        Returns
        -------
        str
            A description of the current step.
        """
        if not P:
            P = self.parameters.values_to_dict()

        text = "Calculating selected RDKit descriptors from configuration(s)."

        return self.header + "\n" + __(text, **P, indent=4 * " ").__str__()

    def run(self):
        """Run a RDKit"""

        system, configuration = self.get_system_configuration(None)
        n_atoms = configuration.n_atoms
        if n_atoms == 0:
            self.logger.error("RDKit run(): there is no structure!")
            raise RuntimeError("RDKit run(): there is no structure!")

        # Print out header to the main output
        printer.important(self.header)
        printer.important("")

        next_node = super().run(printer)
        # Get the values of the parameters, dereferencing any variables
        P = self.parameters.current_values_to_dict(
            context=seamm.flowchart_variables._data
        )

        in_db = P["where"] in ("Database", "Both")
        if in_db:
            properties = configuration.properties
        in_table = P["where"] in ("Table", "Both")
        if in_table:
            table_handle = self.get_variable(P["table"])
            table = table_handle["table"]

        # Print what we are doing
        printer.important(__(self.description_text(P), indent=self.indent))

        # And add the citations for the features used.
        references = set()
        mol = configuration.to_RDKMol()

        for feature in self.parameters["features"].value:
            if feature in Descriptors.__dict__:
                # Add the feature citation(s)
                for citation_id in metadata.properties["2D-Descriptors"][feature][
                    "citations"
                ]:
                    references.add(citation_id)
                value = Descriptors.__dict__[feature](mol)
                if in_table:
                    if feature not in table.columns:
                        table_handle["defaults"][feature] = np.nan
                        table[feature] = np.nan
                    row_index = table_handle["current index"]
                    table.at[row_index, feature] = value
                if in_db:
                    key = "rdkit." + feature
                    if not properties.exists(key):
                        properties.add(
                            key, description="RDKit 2-D descriptor " + feature
                        )
                    properties.put(key, value)
            elif feature in Descriptors3D.__dict__:
                # Add the feature citation(s)
                for citation_id in metadata.properties["3D-Descriptors"][feature][
                    "citations"
                ]:
                    references.add(citation_id)
                value = Descriptors3D.__dict__[feature](mol)
                if in_table:
                    if feature not in table.columns:
                        table_handle["defaults"][feature] = np.nan
                        table[feature] = np.nan
                    row_index = table_handle["current index"]
                    table.at[row_index, feature] = value
                if in_db:
                    key = "rdkit." + feature
                    if not properties.exists(key):
                        properties.add(
                            key, description="RDKit 3-D descriptor " + feature
                        )
                    properties.put(key, value)
            else:
                print(f"     unable to handle feature '{feature}'")

        # Add the references
        for reference in references:
            if reference in self._bibliography:
                self.references.cite(
                    raw=self._bibliography[reference],
                    alias=reference,
                    module="rdkit_step",
                    level=2,
                    note="RDKit feature citation",
                )
            else:
                self.logger.warning(f"Could not find reference '{reference}'")

        return next_node

    def analyze(self, indent="", **kwargs):
        """Do any analysis of the output from this step.

        Also print important results to the local step.out file using
        "printer".

        Parameters
        ----------
        indent: str
            An extra indentation for the output
        """
        printer.normal(
            __(
                "This is a placeholder for the results from the RDKit step",
                indent=4 * " ",
                wrap=True,
                dedent=False,
            )
        )
