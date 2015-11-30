from models.common import DeclEnum


class PositionType(DeclEnum):
    """
    Enumerated categories of football player positions.
    """
    goalkeeper = "Goalkeeper", "Goalkeepers"
    defender = "Defender", "Defending positions"
    midfielder = "Midfielder", "Midfield positions"
    forward = "Forward", "Forward positions"
    unknown = "Unknown", "Unknown player position"


class NameOrderType(DeclEnum):
    """
    Enumerated types of naming order conventions.
    """
    western = "Western", "Western"
    middle = "Middle", "Middle"
    eastern = "Eastern", "Eastern"


class CardType(DeclEnum):
    """
    Enumerated types of disciplinary cards.
    """
    yellow = "Yellow", "Yellow"
    yellow_red = "Yellow/Red", "Yellow/Red"
    red = "Red", "Red"


class SurfaceType(DeclEnum):
    """
    Enumerated types of playing surfaces.
    """
    natural = "Natural", "Natural"
    artificial = "Artificial", "Artificial"
    hybrid = "Hybrid", "Hybrid"


class ShotOutcomeType(DeclEnum):
    """
    Enumerated types of shot outcomes.
    """
    goal = "Goal", "Goal"
    miss = "Miss", "Miss"
    save = "Save", "Save"
    wide = "Wide", "Wide of post"
    over = "Over", "Over crossbar"
    post = "Post", "Hit post"
    bar = "Bar", "Hit bar"


class BodypartType(DeclEnum):
    """
    Enumerated types of body parts.
    """
    left_foot = "Left foot", "Left foot"
    right_foot = "Right foot", "Right foot"
    foot = "Foot", "Foot"
    head = "Head", "Head"
    chest = "Chest", "Chest"
    unknown = "Unknown", "Unknown"


class ShotEventType(DeclEnum):
    """
    Enumerated types of shot events.
    """
    unknown = "Unknown", "Unknown"
    cross_fk = "Cross from free kick", "Cross from free kick"
    cross_ck = "Cross from corner kick", "Cross from corner kick"
    cross_throw = "Cross from throw-in", "Cross from throw-in"
    cross_open_play = "Cross from open play", "Cross from open play"
    olympic = "Direct from corner kick", "Direct from corner kick"
    free_kick = "Direct from free kick", "Direct from free kick"
    flick_ck = "Flick on from corner kick", "Flick on from corner kick"
    flick_fk = "Flick on from direct free kick", "Flick on from direct free kick"
    flick_ifk = "Flick on from indirect free kick", "Flick on from indirect free kick"
    flick_throw = "Flick on from throw-in", "Flick on from throw-in"
    one_v_one = "Through pass creates 1-v-1", "Through pass creates 1-v-1"
    scramble = "Contested scramble", "Contested scramble"
    redirected = "Close-range re-direction", "Close-range re-direction"
    deflection = "Deflected shot", "Deflected shot"
    shot_6_box = "Shot inside goal area", "Shot inside goal area"
    shot_18_box = "Shot inside penalty area", "Shot inside penalty area"
    shot_outside = "Shot outside penalty area", "Shot outside penalty area"
    rebound = "Shot following rebound", "Shot following rebound"
    giveaway = "Shot following defensive giveaway", "Shot following defensive giveaway"
    round_keeper = "Maneuver around goalkeeper", "Maneuver around goalkeeper"


class FoulEventType(DeclEnum):
    """
    Enumerated types of foul events.
    """
    unknown = "Unknown", "Unknown"
    handball = "Handball", "Handball"
    holding = "Holding", "Holding"
    off_ball = "Off-ball infraction", "Off-ball infraction"
    dangerous = "Dangerous play", "Dangerous play"
    reckless = "Reckless challenge", "Reckless challenge"
    over_celebration = "Excessive celebration", "Excessive celebration"
    simulation = "Simulation", "Simulation"
    dissent = "Dissent", "Dissent"
    repeated_fouling = "Persistent infringement", "Persistent infringement"
    delay_restart = "Delaying restart", "Delaying restart"
    encroachment = "Dead ball encroachment", "Dead ball encroachment"
    field_unauthorized = "Unauthorized field entry/exit", "Unauthorized field entry/exit"
    serious_foul_play = "Serious foul play", "Serious foul play"
    violent_conduct = "Violent conduct", "Violent conduct"
    verbal_abuse = "Offensive/abusive language or gestures", "Offensive/abusive language or gestures"
    spitting = "Spitting", "Spitting"
    professional = "Professional foul", "Professional foul"
    unsporting = "Unsporting behavior", "Unsporting behavior"
    handball_block_goal = "Handball denied obvious scoring opportunity", "Handball denied obvious scoring opportunity"


class WeatherConditionType(DeclEnum):
    """
    Enumerated types of NWS/NOAA weather conditions.
    """
    clear = "Clear", "Clear"
    partly_cloudy = "Partly Cloudy", "Partly Cloudy"
    mostly_cloudy = "Mostly Cloudy", "Mostly Cloudy"
    few_clouds = "Few Clouds", "Few Clouds"
    dry_hot = "Hot and Dry", "Hot and Dry"
    humid_hot = "Hot and Humid", "Hot and Humid"
    overcast = "Overcast", "Overcast"
    fog = "Fog/Mist", "Fog/Mist"
    light_rain = "Light Rain", "Light Rain"
    rain = "Rain", "Rain"
    heavy_rain = "Heavy Rain", "Heavy Rain"
    windy_clear = "Clear and Windy", "Clear and Windy"
    windy_mostly_cloudy = "Mostly Cloudy and Windy", "Mostly Cloudy and Windy"
    windy_partly_cloudy = "Partly Cloudy and Windy", "Partly Cloudy and Windy"
    windy_overcast = "Overcast and Windy", "Overcast and Windy"
    flurries = "Snow Flurries", "Snow Flurries"
    light_snow = "Light Snow", "Light Snow"
    heavy_snow = "Heavy Snow", "Heavy Snow"