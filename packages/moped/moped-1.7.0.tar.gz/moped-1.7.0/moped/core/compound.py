"""Compound abstraction."""
from __future__ import annotations

import reprlib
from dataclasses import dataclass, field
from typing import Any, Dict, List, Set

__all__ = ["Compound"]


@dataclass
class Compound:
    base_id: str
    compartment: str
    id: str = ""
    formula: Dict[str, float] = field(default_factory=dict)
    charge: int | None = None
    name: str | None = None
    gibbs0: float | None = None
    smiles: str | None = None
    database_links: Dict[str, Set[str]] = field(default_factory=dict)
    types: List[str] = field(default_factory=list)
    in_reaction: Set[str] = field(default_factory=set)

    def __hash__(self) -> int:
        """Hash the compound id."""
        return hash(self.id)

    def __eq__(self, other: object) -> bool:
        """Compare compound id with another compound id."""
        if not isinstance(other, Compound):
            return False
        return self.id == other.id

    def __iter__(self) -> Any:
        """Return tuple of certain attributes and their value."""
        return (
            (i, getattr(self, i))
            for i in [
                "base_id",
                "id",
                "name",
                "compartment",
                "formula",
                "charge",
                "gibbs0",
                "smiles",
                "types",
                "in_reaction",
                "database_links",
            ]
            if bool(getattr(self, i))
        )

    def __str__(self) -> str:
        """Return string representation."""
        s = f"Compound <{self.id}>"
        for k, v in dict(self).items():
            s += f"\n    {k}: {v}"
        return s

    def __repr__(self) -> str:
        """Return representation."""
        args = ", ".join(f"{k}={reprlib.repr(v)}" for k, v in dict(self).items())
        return f"Compound({args})"

    def formula_to_string(self) -> str:
        """Create a string variant of the formula dict.

        Examples
        --------
        >>> Compound(formula={"C": 1, "H": 1}).formula_to_string()
        "C1H1"

        Returns
        -------
        formula_string: str
            The compound formula as a string representation
        """
        return "".join([str(k) + str(v) for k, v in self.formula.items()])
