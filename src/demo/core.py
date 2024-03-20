"""
This module contains types that define a domain in the SDTM standard.
"""
import enum
from typing import Dict, List, Optional, Type, Union

import pydantic  # type: ignore

# pylint: disable=invalid-name


ValidFieldDatatypes = Union[Type[int], Type[float], Type[str]]
"""allowed datatypes in `VariableSpec` datatype checking"""

ValidDatatypes = Union[int, float, str, None]
"""allowed datatype for data field"""


class VariableType(str, enum.Enum):
    """
    A set of allowed field types defined in the STDM v1.8 guide.
    """

    Identifier = "Identifier"
    """Identifier variables, such as those that identify the study, the subject 
    (individual human or animal or group of individuals) involved in the study, the 
    domain, and the sequence number of the record"""

    Topic = "Topic"
    """Topic variables, which specify the focus of the observation (e.g., the name of a 
    lab test)"""

    Timing = "Timing"
    """Timing variables, which describe the timing of an observation (e.g., start date, 
    end date)"""

    Qualifier = "Qualifier"
    """Qualifier variables, which include additional illustrative text or numeric values
    that describe the results or additional traits of the observation (e.g., units, 
    descriptive adjectives)"""

    Rule = "Rule"
    """Rule variables, which express an algorithm or executable method to define start,
    end, or looping conditions in the Trial Design model."""

    DomainSpecific = "DomainSpecific"
    """Special-case variables available in specific domains."""


class QualifierSubType(str, enum.Enum):
    """
    The Qualifier variables are classified into the following groups. See
    """

    Grouping = "Grouping"
    """Grouping Qualifiers used to group together a collection of observations within 
    the same domain"""

    Result = "Result"
    """Result Qualifiers, which describe the specific results associated with the topic 
    variable in a Findings dataset and which answer the question raised by the topic 
    variable"""

    Synonym = "Synonym"
    """Synonym Qualifiers specifying an alternative name for a particular variable in 
    an observation"""

    Record = "Record"
    """Record Qualifiers, which define additional attributes of the observation record 
    as a whole, rather than describing a particular variable within a record"""

    Variable = "Variable"
    """Variable Qualifiers used to further modify or describe a specific variable within
    an observation and which are only meaningful in the context of the variable they 
    qualify"""


class VariableSpec(pydantic.BaseModel):
    """
    A unit of information in an observation.
    """

    name: str
    """a coded field name"""

    type: VariableType
    """the class of this observation"""

    datatype: ValidFieldDatatypes
    """the type of this field"""

    subtype: Optional[QualifierSubType] = None
    """the variable subtype, if the type is Qualifier"""

    label: Optional[str] = None
    """human-readable variable label"""

    description: Optional[str] = None
    """a description of the field"""


class CoreStatus(str, enum.Enum):
    """
    The concept of core variable is used both as a measure of compliance, and to provide
    general guidance to sponsors. Three categories of variables are specified in the
    “Core” column in the domain models:
      - Required
      - Expected
      - Permissible
    """

    Required = "Required"
    """Variable is required to consider the record valid"""

    Expected = "Expected"
    """Variable must be present, but may have missing values"""

    Permissible = "Permissible"
    """Variable may be present"""


class DomainSpec(pydantic.BaseModel):
    """An observation class"""

    name: str
    """a two-character abbreviation for this domain"""

    label: str
    """a domain description"""

    variables: List[VariableSpec]
    """the variables that this domain contains"""

    core_flags: List[CoreStatus]
    """encodes whether each variable in `variables` must be present"""

    description: Optional[str]
    """a human readable description for this domain"""


class DomainTable(pydantic.BaseModel):
    """Represents a tabular collection of information in a domain"""

    meta: DomainSpec
    """information about the domain"""

    data: Dict[str, Optional[List[ValidDatatypes]]]
    """contains the data encoded in variables"""
