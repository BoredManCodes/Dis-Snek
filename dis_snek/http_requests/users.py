from typing import TYPE_CHECKING, Any

from dis_snek.models.route import Route

if TYPE_CHECKING:
    from dis_snek.models.snowflake import Snowflake_Type


class UserRequests:
    request: Any

    async def get_current_user(self):
        """
        Shortcut to get requester's user.
        """
        return self.get_user("@me")

    async def get_user(self, user_id: "Snowflake_Type") -> dict:
        """
        Get a user object for a given user ID.

        :param user_id: The user to get.
        :return: user
        """
        return await self.request(Route("GET", f"/users/{user_id}"))

    async def modify_user(self, payload: dict) -> dict:
        """
        Modify the user account settings.

        :param payload: The data to send.
        """
        return await self.request(Route("PATCH", f"/users/@me"), data=payload)

    async def get_user_guilds(self) -> list:
        """
        Returns a list of partial guild objects the current user is a member of. Requires the guilds OAuth2 scope.
        """
        return await self.request(Route("GET", f"/users/@me/guilds"))

    async def leave_guild(self, guild_id) -> dict:
        """
        Leave a guild. Returns a 204 empty response on success.

        :param guild_id: The guild to leave from.
        """
        return await self.request(Route("DELETE", f"/users/@me/guilds/{guild_id}"))

    async def create_dm(self, recipient_id) -> dict:
        """
        Create a new DM channel with a user. Returns a DM channel object.

        :param recipient_id: The recipient to open a DM channel with.
        """
        return await self.request(Route("POST", f"/users/@me/channels"), data=dict(recipient_id=recipient_id))

    async def create_group_dm(self, payload: dict) -> dict:
        """
        Create a new group DM channel with multiple users.

        :param payload: The data to send.
        """
        return await self.request(Route("POST", f"/users/@me/channels"), data=payload)

    async def get_user_connections(self) -> list:
        """
        Returns a list of connection objects. Requires the connections OAuth2 scope.
        """
        return await self.request(Route("GET", f"/users/@me/connections"))
