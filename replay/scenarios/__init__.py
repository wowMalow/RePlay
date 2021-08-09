"""
Сценарий --- пайплайн работы с рекомендациями, включающий в себя несколько шагов.
Например, разбиение данных, обучение моделей, подсчет метрик.
"""
from replay.scenarios.fallback import Fallback
from replay.scenarios.basescenario import BaseScenario
from replay.scenarios.two_stages.two_stages_scenario import TwoStagesScenario
from replay.scenarios.two_stages.feature_processor import (
    SecondLevelFeaturesProcessor,
)
