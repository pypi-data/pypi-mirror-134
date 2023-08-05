import re

from rdkit.Chem import Mol
from reinvent_chemistry import Conversions


class AttachmentPointModifier:
    """Manipulate linker SMILES attachment point tokens for compatibility with rdkit calculations"""
    def __init__(self):
        self._conversions = Conversions()

    def extract_attachment_atoms(self, linker_smiles: str) -> list:
        """return a list of all attachment point atoms"""
        # extract all atoms in square brackets
        bracket_atoms = re.findall(r"\[(.*?)\]", linker_smiles)
        # extract only the linker attachment atoms - these atoms have ":" separating the atoms and the label
        attachment_atoms = [attachment_atom for attachment_atom in bracket_atoms if ":" in attachment_atom]

        return attachment_atoms

    def add_explicit_H_to_atom(self, tokens: str) -> str:
        """modifies a SMILES sequence by incrementing the number of explicit hydrogens by 1"""
        # extract the attachment atom tokens without the position label
        attachment_tokens = tokens.split(":")[0]
        modified_attachment = ""

        # if the attachment atom contains only 1 explicit hydrogen, a number will not
        # be present in the SMILES, e.g. "CH". In this case, manually add a "2"
        if self.is_last_token_H(attachment_tokens):
            modified_attachment = attachment_tokens + str(2)
        else:
            for idx, token in enumerate(attachment_tokens):
                try:
                    num_explicit_Hs = int(token)
                    modified_attachment += str(num_explicit_Hs + 1)
                except Exception:
                    modified_attachment += token

        # if the attachment atom has no explicit hydrogens and does not contain a charge, add a hydrogen
        if "H" not in modified_attachment:
            modified_attachment += "H"

        return modified_attachment

    def is_last_token_H(self, tokens: str) -> bool:
        """check if the last token in SMILES sequence is 'H'"""
        return True if tokens[-1] == "H" else False

    def cap_linker_with_hydrogen(self, linker_mol: Mol) -> Mol:
        """cap linker attachment point atoms with an explicit hydrogen"""
        linker_smiles = self._conversions.mol_to_smiles(linker_mol)
        attachment_atoms = self.extract_attachment_atoms(linker_smiles)

        for tokens in attachment_atoms:
            modified_attachment = self.add_explicit_H_to_atom(tokens)
            linker_smiles = linker_smiles.replace(tokens, modified_attachment)

        capped_linker_mol = self._conversions.smile_to_mol(linker_smiles)

        return capped_linker_mol
