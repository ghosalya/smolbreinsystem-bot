from asyncio import get_event_loop


SESSIONS = {
    "DEFAULT": {},   # null or empty string will skip remidner
}


def get_player_name(name):
    if not name.startswith("@"):
        return "@" + name
    else:
        return name


def next_turn(*args, **kwargs):
    """
    Set reminder for next turn. The tagged player will be reminded at
    8pm every day.

    Usage:

        * `$nextturn @player` - set the tagged player for the DEFAULT session.
        * `$nextturn @player #game` - set the tagged player for session named `#game`.
                If game session doesn't exists, a new one will be created. Note that
                game must start with `#`
    """

    try:
        channel = kwargs.get("channel")
        if not channel:
            return "Must come from a channel (discord server)."

        channel_id = channel.id

        if len(args) == 0:
            return "Please provide player name (e.g. `$nextturn @player`)"

        if len(args) == 1:
            reminder = dict(
                message = get_player_name(args[0]),
                channel = channel,
            )
            channel_sessions = SESSIONS.get(channel_id, {})
            channel_sessions["DEFAULT"] = reminder
            SESSIONS[channel_id] = channel_sessions
            return "Reminder set for " + channel_sessions["DEFAULT"]["message"] + "!"

            
        if len(args) >= 2:
            session = args[1]
            if not session.startswith("#"):
                return "Game session name must start with `#` (e.g. `$nextturn @player #game`)"
            
            reminder = dict(
                message = get_player_name(args[0]),
                channel = channel,
            )
            
            channel_sessions = SESSIONS.get(channel_id, {})
            channel_sessions[session] = reminder
            SESSIONS[channel_id] = channel_sessions
            return "Reminder set for " + channel_sessions[session]["message"] + " (for session " + session + ")" + "!"

    
    except Exception as e:
        raise e
        return "NextTurn error: " + str(e)


def clear_turn(*args, **kwargs):
    try:
        channel = kwargs.get("channel")
        if not channel:
            return "Must come from a channel (discord server)."

        channel_id = channel.id
        if len(args) == 0:
            channel_sessions = SESSIONS.get(channel_id, {})
            channel_sessions["DEFAULT"] = None
            SESSIONS[channel_id] = channel_sessions
            return "NextTurn: default session cleared."

        if len(args) == 1:
            session = args[0]
            if not session.startswith("#"):
                return "Game session name must start with `#` (e.g. `$nextturn @player #game`)"
            
            channel_sessions = SESSIONS.get(channel_id, {})
            channel_sessions[session] = None
            SESSIONS[channel_id] = channel_sessions
            return "NextTurn: session " + session + " cleared."

    except Exception as e:
        return "NextTurn clear error: " + str(e)


def remind():
    for channel_id, sessions in SESSIONS.items():
        for session_name, reminder in sessions:
            if session_name == "DEFAULT":
                try:
                    reminder["channel"].send(
                        "Reminder for: " + reminder["message"]
                    )
                except:
                    continue
            else:
                try:
                    reminder["channel"].send(
                        "(" + session_name + ")Reminder for: " + reminder["message"]
                    )
                except:
                    continue