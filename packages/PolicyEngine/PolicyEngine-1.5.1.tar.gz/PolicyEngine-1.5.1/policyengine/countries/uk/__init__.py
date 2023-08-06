from pathlib import Path
from openfisca_uk import (
    Microsimulation,
    IndividualSim,
    CountryTaxBenefitSystem,
)
from openfisca_uk.entities import *
from openfisca_uk_data import FRSEnhanced, SynthFRS
from policyengine.utils.general import PolicyEngineResultsConfig
from policyengine.countries.country import PolicyEngineCountry
from policyengine.countries.uk.default_reform import create_default_reform
import os

UK_FOLDER = Path(__file__).parent


class UKResultsConfig(PolicyEngineResultsConfig):
    net_income_variable: str = "net_income"
    in_poverty_variable: str = "in_poverty_bhc"
    household_net_income_variable: str = "household_net_income"
    equiv_household_net_income_variable: str = "equiv_household_net_income"
    child_variable: str = "is_child"
    working_age_variable: str = "is_WA_adult"
    senior_variable: str = "is_SP_age"
    person_variable: str = "people"
    tax_variable: str = "household_tax"
    benefit_variable: str = "household_benefits"
    employment_income_variable: str = "employment_income"
    self_employment_income_variable: str = "self_employment_income"
    total_income_variable: str = "total_income"


class UK(PolicyEngineCountry):
    name = "uk"
    system = CountryTaxBenefitSystem
    Microsimulation = Microsimulation
    IndividualSim = IndividualSim
    default_dataset = FRSEnhanced
    default_dataset_year = 2019
    default_reform = create_default_reform()
    parameter_file = UK_FOLDER / "reform_parameters.yaml"
    default_household_file = UK_FOLDER / "default_household.yaml"
    entity_hierarchy_file = UK_FOLDER / "entities.yaml"
    version = "0.2.0"
    results_config = UKResultsConfig

    def __init__(self):
        if (
            "POLICYENGINE_SYNTH_UK" in os.environ
            and os.environ["POLICYENGINE_SYNTH_UK"]
        ):
            self.default_dataset = SynthFRS
            if len(SynthFRS.years) == 0:
                # No synthetic data - download from GitHub
                SynthFRS.save(year=2019)
        super().__init__()
