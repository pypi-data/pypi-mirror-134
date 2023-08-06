from typing import Optional, Union, List

from slapp_py.core_classes.simple_source import SimpleSource

from slapp_py.core_classes.socials.social import Social

BATTLEFY_BASE_ADDRESS = "battlefy.com/teams"


class BattlefyTeamSocial(Social):
    def __init__(self,
                 persistent_team_id: Optional[str] = None,
                 sources: Union[None, SimpleSource, List[SimpleSource]] = None):
        super().__init__(
            value=persistent_team_id,
            sources=sources,
            social_base_address=BATTLEFY_BASE_ADDRESS
        )

    @staticmethod
    def from_dict(obj: dict) -> 'BattlefyTeamSocial':
        assert isinstance(obj, dict)
        social = Social._from_dict(obj, BATTLEFY_BASE_ADDRESS)
        return BattlefyTeamSocial(social.handle, social.sources)
