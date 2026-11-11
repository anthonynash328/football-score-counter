from drafter import *
from dataclasses import dataclass
from bakery import assert_equal

@dataclass
class Team:
    name: str
    color: str

@dataclass
class State:
    away_team: Team
    home_team: Team
    away_score: int
    home_score: int
    away_field_goal_att: int
    away_field_goal_made: int
    home_field_goal_att: int
    home_field_goal_made: int
    away_conversion_att: int
    away_conversion_made: int
    home_conversion_att: int
    home_conversion_made: int
    away_punt: int
    home_punt: int
    away_turnover: int
    home_turnover: int
    second_half_team: Team
    
@route
def index(state: State) -> Page:
    '''
    the homepage;
    takes user's press of button and returns the away team selection page
    '''
    return Page(state,[
        "Hello! Welcome to my online football-scoring website.","\n",
        "This website is intended to be used during football games,","\n",
        "particularly NFL games, and thus follows NFL rules.","\n",
        "Have fun!",
        change_background_color(Button("Start team selection","away_team_selection"),"gray")
        ])
assert_equal(index(State(Team("",""),Team("",""),0,0,0,0,0,0,0,0,0,0,0,0,0,0,Team("",""))),
             Page(State(Team("",""),Team("",""),0,0,0,0,0,0,0,0,0,0,0,0,0,0,Team("","")),[
        "Hello! Welcome to my online football-scoring website.","\n",
        "This website is intended to be used during football games,","\n",
        "particularly NFL games, and thus follows NFL rules.","\n",
        "Have fun!",
        change_background_color(Button("Start team selection","away_team_selection"),"gray")
        ]))
    
@route
def away_team_selection(state: State) -> Page:
    '''
    resets all variables to 0,
    presents user with all 8 divisions to select away team, plus custom button;
    user's press of button returns a division page
    '''
    state.home_score = 0
    state.away_score = 0
    state.away_field_goal_att = 0
    state.away_field_goal_made = 0
    state.home_field_goal_att = 0
    state.home_field_goal_made = 0
    state.away_conversion_att = 0
    state.away_conversion_made = 0
    state.home_conversion_att = 0
    state.home_conversion_made = 0
    state.away_punt = 0
    state.home_punt = 0
    state.away_turnover = 0
    state.home_turnover = 0
    state.away_team = Team("","")
    state.home_team = Team("","")
    return Page(state, [
        "Select away team's division: ",
        "\n",
        change_background_color(Button("NFC East","nfc_east"),"blue"),
        change_background_color(Button("NFC South","nfc_south"),"blue"),
        change_background_color(Button("NFC West","nfc_west"),"blue"),
        change_background_color(Button("NFC North","nfc_north"),"blue"),
        "\n",
        change_background_color(Button("AFC East","afc_east"),"red"),
        change_background_color(Button("AFC South","afc_south"),"red"),
        change_background_color(Button("AFC West","afc_west"),"red"),
        change_background_color(Button("AFC North","afc_north"),"red"),
        "\n",
        change_background_color(Button("Custom Away Team","custom_away"),"gray")
        ])

@route
def home_team_selection(state: State) -> Page:
    '''
    presents user with all 8 divsions and custom button to pick home team;
    takes user's press of button and returns a division page
    '''
    return Page(state, [
        "Select home team's division: ",
        "\n",
        change_background_color(Button("NFC East","nfc_east2"),"blue"),
        change_background_color(Button("NFC South","nfc_south2"),"blue"),
        change_background_color(Button("NFC West","nfc_west2"),"blue"),
        change_background_color(Button("NFC North","nfc_north2"),"blue"),
        "\n",
        change_background_color(Button("AFC East","afc_east2"),"red"),
        change_background_color(Button("AFC South","afc_south2"),"red"),
        change_background_color(Button("AFC West","afc_west2"),"red"),
        change_background_color(Button("AFC North","afc_north2"),"red"),
        "\n",
        change_background_color(Button("Custom Home Team","custom_home"),"gray")
        ])

@route
def custom_away(state: State) -> Page:
    '''
    lets user create name and color for away team;
    inputs: name and color
    returns: new state variables
    '''
    return Page(state,[
        "Enter team name: ",TextBox("customaway",state.away_team.name),"\n",
        "Enter team color in hexcode: ",TextBox("awaycolor",state.away_team.color),"\n",
        change_background_color(Button("What is hexcode?","away_hexcode_page"),"gray"),"\n",
        change_background_color(Button("Submit","custom_away_submit"),"gray")
        ])

@route
def away_hexcode_page(state: State) -> Page:
    '''
    explains hexcode rules to user;
    no inputs, returns the user to custom away page
    '''
    return Page(state,[
        "Hexcode is a numerical way of recording colors. In hexcode, "
        "colors are represented by a '#' followed by six numbers or letters a to f, where 0 is the lowest and f is the highest. ",
        "The hexcode number itself is made up of three groups of two, where the groups represent red, green, and blue respectively. ",
        "For example, the hexcode #0066ff shows us that red (00) is not present, green (66) ",
        "is somewhere in the middle, and blue (ff) is at its max value. ",
        "The resulting color is a mix of green and blue that is mostly blue: ","\n",
        change_background_color(Button("Return to Custom Team Page","custom_away"),"#0066ff")
        ])

@route
def custom_away_submit(state: State, customaway: str, awaycolor: str) -> Page:
    '''
    sets away team variables to those custom-made by user;
    sends user to home team selection page
    '''
    state.away_team.name = customaway
    state.away_team.color = awaycolor
    return home_team_selection(state)

@route
def custom_home(state: State) -> Page:
    '''
    lets user create name and color for home team;
    inputs: name and color
    returns: new state variables
    '''
    return Page(state,[
        "Enter team name: ",TextBox("customhome",state.home_team.name),"\n",
        "Enter team color in hexcode: ",TextBox("homecolor",state.home_team.color),"\n",
        change_background_color(Button("What is hexcode?","home_hexcode_page"),"gray"),"\n",
        change_background_color(Button("Submit","custom_home_submit"),"gray")
        ])

@route
def home_hexcode_page(state: State) -> Page:
    '''
    explains hexcode rules to user;
    returns them to custom home team page
    '''
    return Page(state,[
        "Hexcode is a numerical way of recording colors. In hexcode, "
        "colors are represented by a '#' followed by six numbers or letters a to f, where 0 is the lowest and f is the highest. ",
        "The hexcode number itself is made up of three groups of two, where the groups represent red, green, and blue respectively. ",
        "For example, the hexcode #ff7700 shows us that red (ff) is at its max, green (77) ",
        "is somewhere in the middle, and blue (00) is not present at all. ",
        "The resulting color is a mix of red and green that is mostly red: ","\n",
        change_background_color(Button("Return to Custom Team Page","custom_home"),"#ff7700")
        ])

@route
def custom_home_submit(state: State, customhome: str, homecolor: str) -> Page:
    '''
    sets home team variables to those made by user;
    sends user to cointoss page
    '''
    state.home_team.name = customhome
    state.home_team.color = homecolor
    return cointoss(state)

@route
def back(state: State) -> Page:
    '''
    lets user exit a division's page, returning them to division selection page
    '''
    return away_team_selection(state)

@route
def nfc_east(state: State) -> Page:
    '''
    shows user their selected division, and prompts them to pick a team;
    input: button press
    returns: new state team variables
    '''
    return Page(state, [
        "Pick away team: ","\n",
        change_background_color(Button("Eagles","eagles"),"#004953"),
        change_background_color(Button("Cowboys","cowboys"),"#003594"),
        change_background_color(Button("Giants","giants"),"#0b2265"),
        change_background_color(Button("Commanders","commanders"),"#5a1414"),"\n",
        change_background_color(Button("Back","back"),"gray")
        ])

@route
def eagles(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Eagles"
    state.away_team.color = "#004953"
    return home_team_selection(state)

@route
def cowboys(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Cowboys"
    state.away_team.color = "#003594"
    return home_team_selection(state)

@route
def giants(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Giants"
    state.away_team.color = "#0b2265"
    return home_team_selection(state)

@route
def commanders(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Commanders"
    state.away_team.color = "#5a1414"
    return home_team_selection(state)

@route
def nfc_south(state: State) -> Page:
    '''
    shows user their selected division, and prompts them to pick a team;
    input: button press
    returns: new state team variables
    '''
    return Page(state, [
        "Pick away team: ","\n",
        change_background_color(Button("Panthers","panthers"),"#0085ca"),
        change_background_color(Button("Falcons","falcons"),"#a71930"),
        change_background_color(Button("Saints","saints"),"#d3bc8d"),
        change_background_color(Button("Buccaneers","buccaneers"),"#d50a0a"),"\n",
        change_background_color(Button("Back","back"),"gray")
        ])

@route
def panthers(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Panthers"
    state.away_team.color = "#0085ca"
    return home_team_selection(state)

@route
def falcons(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Falcons"
    state.away_team.color = "#a71930"
    return home_team_selection(state)

@route
def saints(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Saints"
    state.away_team.color = "#d3bc8d"
    return home_team_selection(state)

@route
def buccaneers(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Buccaneers"
    state.away_team.color = "#d50a0a"
    return home_team_selection(state)

@route
def nfc_west(state: State) -> Page:
    '''
    shows user their selected division, and prompts them to pick a team;
    input: button press
    returns: new state team variables
    '''
    return Page(state, [
        "Pick away team: ","\n",
        change_background_color(Button("Rams","rams"),"#003594"),
        change_background_color(Button("Seahawks", "seahawks"),"#69be28"),
        change_background_color(Button("Forty-Niners","fortyniners"),"#b3995d"),
        change_background_color(Button("Cardinals","cardinals"),"#97233f"),"\n",
        change_background_color(Button("Back","back"),"gray")
        ])

@route
def rams(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Rams"
    state.away_team.color = "#003594"
    return home_team_selection(state)

@route
def seahawks(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Seahawks"
    state.away_team.color = "#69be28"
    return home_team_selection(state)

@route
def fortyniners(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Forty-Niners"
    state.away_team.color = "#b3995d"
    return home_team_selection(state)

@route
def cardinals(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Cardinals"
    state.away_team.color = "#97233f"
    return home_team_selection(state)

@route
def nfc_north(state: State) -> Page:
    '''
    shows user their selected division, and prompts them to pick a team;
    input: button press
    returns: new state team variables
    '''
    return Page(state, [
        "Pick away team: ","\n",
        change_background_color(Button("Lions","lions"),"#0076b6"),
        change_background_color(Button("Packers", "packers"),"#203731"),
        change_background_color(Button("Bears","bears"),"#c83803"),
        change_background_color(Button("Vikings","vikings"),"#4f2683"),"\n",
        change_background_color(Button("Back","back"),"gray")
        ])

@route
def lions(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Lions"
    state.away_team.color = "#0076b6"
    return home_team_selection(state)

@route
def packers(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Packers"
    state.away_team.color = "#203731"
    return home_team_selection(state)

@route
def bears(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Bears"
    state.away_team.color = "#c83803"
    return home_team_selection(state)

@route
def vikings(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Vikings"
    state.away_team.color = "#4f2683"
    return home_team_selection(state)

@route
def afc_east(state: State) -> Page:
    '''
    shows user their selected division, and prompts them to pick a team;
    input: button press
    returns: new state team variables
    '''
    return Page(state, [
        "Pick away team: ","\n",
        change_background_color(Button("Patriots", "patriots"),"#002244"),
        change_background_color(Button("Bills", "bills"),"#c60c30"),
        change_background_color(Button("Jets","jets"),"#125740"),
        change_background_color(Button("Dolphins","dolphins"),"#008e97"),"\n",
        change_background_color(Button("Back","back"),"gray")
        ])

@route
def patriots(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Patriots"
    state.away_team.color = "#002244"
    return home_team_selection(state)

@route
def bills(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Bills"
    state.away_team.color = "#c60c30"
    return home_team_selection(state)

@route
def jets(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Jets"
    state.away_team.color = "#125740"
    return home_team_selection(state)

@route
def dolphins(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Dolphins"
    state.away_team.color = "#008e97"
    return home_team_selection(state)

@route
def afc_south(state: State) -> Page:
    '''
    shows user their selected division, and prompts them to pick a team;
    input: button press
    returns: new state team variables
    '''
    return Page(state, [
        "Pick away team: ","\n",
        change_background_color(Button("Jaguars", "jaguars"),"#006778"),
        change_background_color(Button("Texans", "texans"),"#03202f"),
        change_background_color(Button("Titans","titans"),"#4b92db"),
        change_background_color(Button("Colts","colts"),"#002c5f"),"\n",
        change_background_color(Button("Back","back"),"gray")
        ])

@route
def jaguars(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Jaguars"
    state.away_team.color = "#006778"
    return home_team_selection(state)

@route
def texans(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Texans"
    state.away_team.color = "#03202f"
    return home_team_selection(state)

@route
def titans(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Titans"
    state.away_team.color = "#4b92db"
    return home_team_selection(state)

@route
def colts(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Colts"
    state.away_team.color = "#002c5f"
    return home_team_selection(state)

@route
def afc_west(state: State) -> Page:
    '''
    shows user their selected division, and prompts them to pick a team;
    input: button press
    returns: new state team variables
    '''
    return Page(state, [
        "Pick away team: ","\n",
        change_background_color(Button("Broncos", "broncos"),"#fb4f14"),
        change_background_color(Button("Chiefs", "chiefs"),"#e31837"),
        change_background_color(Button("Raiders","raiders"),"#a5acaf"),
        change_background_color(Button("Chargers","chargers"),"#0080c6"),"\n",
        change_background_color(Button("Back","back"),"gray")
        ])

@route
def broncos(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Broncos"
    state.away_team.color = "#fb1414"
    return home_team_selection(state)

@route
def chiefs(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Chiefs"
    state.away_team.color = "#e31837"
    return home_team_selection(state)

@route
def raiders(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Raiders"
    state.away_team.color = "#a5acaf"
    return home_team_selection(state)

@route
def chargers(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Chargers"
    state.away_team.color = "#0080c6"
    return home_team_selection(state)

@route
def afc_north(state: State) -> Page:
    '''
    shows user their selected division, and prompts them to pick a team;
    input: button press
    returns: new state team variables
    '''
    return Page(state, [
        "Pick away team: ","\n",
        change_background_color(Button("Ravens", "ravens"),"#241773"),
        change_background_color(Button("Steelers", "steelers"),"#ffb612"),
        change_background_color(Button("Browns","browns"),"#311d00"),
        change_background_color(Button("Bengals","bengals"),"#fb4f14"),"\n",
        change_background_color(Button("Back","back"),"gray")
        ])

@route
def ravens(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Ravens"
    state.away_team.color = "#241773"
    return home_team_selection(state)

@route
def steelers(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Steelers"
    state.away_team.color = "#ffb612"
    return home_team_selection(state)

@route
def browns(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Browns"
    state.away_team.color = "#331d00"
    return home_team_selection(state)

@route
def bengals(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.away_team.name = "Bengals"
    state.away_team.color = "#fb1414"
    return home_team_selection(state)

@route
def back2(state: State) -> Page:
    return home_team_selection(state)

@route
def nfc_east2(state: State) -> Page:
    '''
    shows user their selected division, and prompts them to pick a team;
    input: button press
    returns: new state team variables
    '''
    return Page(state, [
        "Pick away team: ","\n",
        change_background_color(Button("Eagles","eagles2"),"#004953"),
        change_background_color(Button("Cowboys","cowboys2"),"#003594"),
        change_background_color(Button("Giants","giants2"),"#0b2265"),
        change_background_color(Button("Commanders","commanders2"),"#5a1414"),"\n",
        change_background_color(Button("Back","back2"),"gray")
        ])

@route
def eagles2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Eagles"
    state.home_team.color = "#004953"
    return cointoss(state)

@route
def cowboys2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Cowboys"
    state.home_team.color = "#003594"
    return cointoss(state)

@route
def giants2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Giants"
    state.home_team.color = "#0b2265"
    return cointoss(state)

@route
def commanders2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Commanders"
    state.home_team.color = "#5a1414"
    return cointoss(state)

@route
def nfc_south2(state: State) -> Page:
    '''
    shows user their selected division, and prompts them to pick a team;
    input: button press
    returns: new state team variables
    '''
    return Page(state, [
        "Pick away team: ","\n",
        change_background_color(Button("Panthers","panthers2"),"#0085ca"),
        change_background_color(Button("Falcons","falcons2"),"#a71930"),
        change_background_color(Button("Saints","saints2"),"#d3bc8d"),
        change_background_color(Button("Buccaneers","buccaneers2"),"#d50a0a"),"\n",
        change_background_color(Button("Back","back2"),"gray")
        ])

@route
def panthers2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Panthers"
    state.home_team.color = "#0085ca"
    return cointoss(state)

@route
def falcons2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Falcons"
    state.home_team.color = "#a71930"
    return cointoss(state)

@route
def saints2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Saints"
    state.home_team.color = "#d3bc8d"
    return cointoss(state)

@route
def buccaneers2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Buccaneers"
    state.home_team.color = "#d50a0a"
    return cointoss(state)

@route
def nfc_west2(state: State) -> Page:
    '''
    shows user their selected division, and prompts them to pick a team;
    input: button press
    returns: new state team variables
    '''
    return Page(state, [
        "Pick away team: ","\n",
        change_background_color(Button("Rams","rams2"),"#003594"),
        change_background_color(Button("Seahawks", "seahawks2"),"#69be28"),
        change_background_color(Button("Forty-Niners","fortyniners2"),"#b3995d"),
        change_background_color(Button("Cardinals","cardinals2"),"#97233f"),"\n",
        change_background_color(Button("Back","back2"),"gray")
        ])

@route
def rams2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Rams"
    state.home_team.color = "#003594"
    return cointoss(state)

@route
def seahawks2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Seahawks"
    state.home_team.color = "#69be28"
    return cointoss(state)

@route
def fortyniners2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Forty-Niners"
    state.home_team.color = "#b3995d"
    return cointoss(state)

@route
def cardinals2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Cardinals"
    state.home_team.color = "#97233f"
    return cointoss(state)

@route
def nfc_north2(state: State) -> Page:
    '''
    shows user their selected division, and prompts them to pick a team;
    input: button press
    returns: new state team variables
    '''
    return Page(state, [
        "Pick away team: ","\n",
        change_background_color(Button("Lions","lions2"),"#0076b6"),
        change_background_color(Button("Packers", "packers2"),"#203731"),
        change_background_color(Button("Bears","bears2"),"#c83803"),
        change_background_color(Button("Vikings","vikings2"),"#4f2683"),"\n",
        change_background_color(Button("Back","back2"),"gray")
        ])

@route
def lions2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Lions"
    state.home_team.color = "#0076b6"
    return cointoss(state)

@route
def packers2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Packers"
    state.home_team.color = "#203731"
    return cointoss(state)

@route
def bears2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Bears"
    state.home_team.color = "#c83803"
    return cointoss(state)

@route
def vikings2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Vikings"
    state.home_team.color = "#4f2683"
    return cointoss(state)

@route
def afc_east2(state: State) -> Page:
    '''
    shows user their selected division, and prompts them to pick a team;
    input: button press
    returns: new state team variables
    '''
    return Page(state, [
        "Pick home team: ","\n",
        change_background_color(Button("Patriots", "patriots2"),"#002244"),
        change_background_color(Button("Bills", "bills2"),"#c60c30"),
        change_background_color(Button("Jets","jets2"),"#125740"),
        change_background_color(Button("Dolphins","dolphins2"),"#008e97"),"\n",
        change_background_color(Button("Back","back2"),"gray")
        ])

@route
def patriots2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Patriots"
    state.home_team.color = "#002244"
    return cointoss(state)

@route
def bills2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Bills"
    state.home_team.color = "#c60c30"
    return cointoss(state)

@route
def jets2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Jets"
    state.home_team.color = "#125740"
    return cointoss(state)

@route
def dolphins2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Dolphins"
    state.home_team.color = "#008e97"
    return cointoss(state)

@route
def afc_south2(state: State) -> Page:
    '''
    shows user their selected division, and prompts them to pick a team;
    input: button press
    returns: new state team variables
    '''
    return Page(state, [
        "Pick home team: ","\n",
        change_background_color(Button("Jaguars", "jaguars2"),"#006778"),
        change_background_color(Button("Texans", "texans2"),"#03202f"),
        change_background_color(Button("Titans","titans2"),"#4b92db"),
        change_background_color(Button("Colts","colts2"),"#002c5f"),"\n",
        change_background_color(Button("Back","back2"),"gray")
        ])

@route
def jaguars2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Jaguars"
    state.home_team.color = "#006778"
    return cointoss(state)

@route
def texans2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Texans"
    state.home_team.color = "#03202f"
    return cointoss(state)

@route
def titans2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Titans"
    state.home_team.color = "#4b92db"
    return cointoss(state)

@route
def colts2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Colts"
    state.home_team.color = "#002c5f"
    return cointoss(state)

@route
def afc_west2(state: State) -> Page:
    '''
    shows user their selected division, and prompts them to pick a team;
    input: button press
    returns: new state team variables
    '''
    return Page(state, [
        "Pick home team: ","\n",
        change_background_color(Button("Broncos", "broncos2"),"#fb4f14"),
        change_background_color(Button("Chiefs", "chiefs2"),"#e31837"),
        change_background_color(Button("Raiders","raiders2"),"#a5acaf"),
        change_background_color(Button("Chargers","chargers2"),"#0080c6"),"\n",
        change_background_color(Button("Back","back2"),"gray")
        ])

@route
def broncos2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Broncos"
    state.home_team.color = "#fb1414"
    return cointoss(state)

@route
def chiefs2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Chiefs"
    state.home_team.color = "#e31837"
    return cointoss(state)

@route
def raiders2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Raiders"
    state.home_team.color = "#a5acaf"
    return cointoss(state)

@route
def chargers2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Chargers"
    state.home_team.color = "#0080c6"
    return cointoss(state)

@route
def afc_north2(state: State) -> Page:
    '''
    shows user their selected division, and prompts them to pick a team;
    input: button press
    returns: new state team variables
    '''
    return Page(state, [
        "Pick home team: ","\n",
        change_background_color(Button("Ravens", "ravens2"),"#241773"),
        change_background_color(Button("Steelers", "steelers2"),"#ffb612"),
        change_background_color(Button("Browns","browns2"),"#311d00"),
        change_background_color(Button("Bengals","bengals2"),"#fb4f14"),"\n",
        change_background_color(Button("Back","back2"),"gray")
        ])

@route
def ravens2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Ravens"
    state.home_team.color = "#241773"
    return cointoss(state)

@route
def steelers2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Steelers"
    state.home_team.color = "#ffb612"
    return cointoss(state)

@route
def browns2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Browns"
    state.home_team.color = "#331d00"
    return cointoss(state)

@route
def bengals2(state: State) -> Page:
    '''
    sets state team variable to user's selected team
    '''
    state.home_team.name = "Bengals"
    state.home_team.color = "#fb1414"
    return cointoss(state)

@route
def cointoss(state: State) -> Page:
    '''
    lets user input which team starts with the ball for the game they are scorekeeping;
    returns the scorekeeping page for whatever team is first
    '''
    return Page(state, [
        "Select the team that starts with the ball: ","\n",
        change_background_color(Button(state.away_team.name, "away_team_starts"),state.away_team.color),
        change_background_color(Button(state.home_team.name, "home_team_starts"),state.home_team.color)
        ])

@route
def away_team_starts(state: State) -> Page:
    '''
    designates the home team as starting the second half,
    then sends the user to the away team scorekeeper
    '''
    state.second_half_team.name = state.home_team.name
    return away_scorekeeper(state)

@route
def home_team_starts(state: State) -> Page:
    '''
    designates the away team as starting the second half,
    then sends the user to the home team scorekeeper
    '''
    state.second_half_team.name = state.away_team.name
    return home_scorekeeper(state)

@route
def away_scorekeeper(state: State) -> Page:
    '''
    allows user to update points for the away team in the 1st half
    '''
    return Page(state, [
        "Current score: ", state.away_team.name, str(state.away_score), "-", str(state.home_score), state.home_team.name, "\n",
        change_background_color(Button("Touchdown", "away_touchdown"), state.away_team.color),
        change_background_color(Button("Field Goal", "away_field_goal_page"), state.away_team.color),
        change_background_color(Button("Punt","away_punt"),state.away_team.color),
        change_background_color(Button("Turnover","away_turnover"),state.away_team.color),
        change_background_color(Button("4th Down Fail","away_turnover_on_downs"),state.away_team.color),
        change_background_color(Button("Safety", "home_safety"), "black"), "\n",
        change_background_color(Button("Halftime","halftime"), "gray")
    ])

@route
def home_scorekeeper(state: State) -> Page:
    '''
    allows user to update points for the home team in the 1st half
    '''
    return Page(state, [
        "Current score: ", state.away_team.name, str(state.away_score), "-", str(state.home_score), state.home_team.name, "\n",
        change_background_color(Button("Safety", "away_safety"), "black"),
        change_background_color(Button("4th Down Fail","home_turnover_on_downs"),state.home_team.color),
        change_background_color(Button("Turnover","home_turnover"),state.home_team.color),
        change_background_color(Button("Punt","home_punt"),state.home_team.color),
        change_background_color(Button("Field Goal", "home_field_goal_page"), state.home_team.color),
        change_background_color(Button("Touchdown", "home_touchdown"), state.home_team.color),"\n",
        change_background_color(Button("Halftime","halftime"), "gray")
    ])

@route
def away_scorekeeper_2(state: State) -> Page:
    '''
    allows user to update points for the away team in the 2nd half
    '''
    return Page(state, [
        "Current score: ", state.away_team.name, str(state.away_score), "-", str(state.home_score), state.home_team.name, "\n",
        change_background_color(Button("Touchdown", "away_touchdown_2"), state.away_team.color),
        change_background_color(Button("Field Goal", "away_field_goal_page_2"), state.away_team.color),
        change_background_color(Button("Punt","away_punt_2"),state.away_team.color),
        change_background_color(Button("Turnover","away_turnover_2"),state.away_team.color),
        change_background_color(Button("4th Down Fail","away_turnover_on_downs_2"),state.away_team.color),
        change_background_color(Button("Safety", "home_safety_2"), "black"), "\n",
        change_background_color(Button("End Game","overtime_cointoss"), "gray")
    ])

@route
def home_scorekeeper_2(state: State) -> Page:
    '''
    allows user to update points for the home team in the 2nd half
    '''
    return Page(state, [
        "Current score: ", state.away_team.name, str(state.away_score), "-", str(state.home_score), state.home_team.name, "\n",
        change_background_color(Button("Safety", "away_safety_2"), "black"),
        change_background_color(Button("4th Down Fail","home_turnover_on_downs_2"),state.home_team.color),
        change_background_color(Button("Turnover","home_turnover_2"),state.home_team.color),
        change_background_color(Button("Punt","home_punt_2"),state.home_team.color),
        change_background_color(Button("Field Goal", "home_field_goal_page_2"), state.home_team.color),
        change_background_color(Button("Touchdown", "home_touchdown_2"), state.home_team.color),"\n",
        change_background_color(Button("End Game","overtime_cointoss"), "gray")
    ])

@route
def away_touchdown(state: State) -> Page:
    '''
    adds 6 to the away team's points
    '''
    state.away_score = state.away_score + 6
    return Page(state, [
        "The", state.away_team.name, "have scored a touchdown; attempt one or two point conversion", "\n",
        change_background_color(Button("+1","away_one_point"), state.away_team.color),
        change_background_color(Button("+2","away_two_points"), state.away_team.color),
        change_background_color(Button("Fail","away_fail"), "gray")
        ])

@route
def home_touchdown(state: State) -> Page:
    '''
    adds 6 to the home team's points
    '''
    state.home_score = state.home_score + 6
    return Page(state, [
        "The", state.home_team.name, "have scored a touchdown; attempt one or two point conversion", "\n",
        change_background_color(Button("+1","home_one_point"), state.home_team.color),
        change_background_color(Button("+2","home_two_points"), state.home_team.color),
        change_background_color(Button("Fail","home_fail"), "gray")
        ])

@route
def away_touchdown_2(state: State) -> Page:
    '''
    adds 6 to the away team's points
    '''
    state.away_score = state.away_score + 6
    return Page(state, [
        "The", state.away_team.name, "have scored a touchdown; attempt one or two point conversion", "\n",
        change_background_color(Button("+1","away_one_point_2"), state.away_team.color),
        change_background_color(Button("+2","away_two_points_2"), state.away_team.color),
        change_background_color(Button("Fail","away_fail_2"), "gray")
        ])

@route
def home_touchdown_2(state: State) -> Page:
    '''
    adds 6 to the home team's points
    '''
    state.home_score = state.home_score + 6
    return Page(state, [
        "The", state.home_team.name, "have scored a touchdown; attempt one or two point conversion", "\n",
        change_background_color(Button("+1","home_one_point_2"), state.home_team.color),
        change_background_color(Button("+2","home_two_points_2"), state.home_team.color),
        change_background_color(Button("Fail","home_fail_2"), "gray")
        ])

@route
def away_touchdown_OT(state: State) -> Page:
    '''
    adds 6 to the away team's points
    '''
    state.away_score = state.away_score + 6
    return Page(state, [
        "The", state.away_team.name, "have scored a touchdown; attempt one or two point conversion", "\n",
        change_background_color(Button("+1","away_one_point_OT"), state.away_team.color),
        change_background_color(Button("+2","away_two_points_OT"), state.away_team.color),
        change_background_color(Button("Fail","away_fail_OT"), "gray")
        ])

@route
def home_touchdown_OT(state: State) -> Page:
    '''
    adds 6 to the home team's points
    '''
    state.home_score = state.home_score + 6
    return Page(state, [
        "The", state.home_team.name, "have scored a touchdown; attempt one or two point conversion", "\n",
        change_background_color(Button("+1","home_one_point_OT"), state.home_team.color),
        change_background_color(Button("+2","home_two_points_OT"), state.home_team.color),
        change_background_color(Button("Fail","home_fail_OT"), "gray")
        ])

@route
def away_fail(state: State) -> Page:
    '''
    after touchdown, updates touchdown conversion data,
    returns other team's scorekeeper
    '''
    state.away_conversion_att += 1
    return home_scorekeeper(state)

@route
def home_fail(state: State) -> Page:
    '''
    after touchdown, updates touchdown conversion data,
    returns other team's scorekeeper
    '''
    state.home_conversion_att += 1
    return away_scorekeeper(state)

@route
def away_fail_2(state: State) -> Page:
    '''
    after touchdown, updates touchdown conversion data,
    returns other team's scorekeeper
    '''
    state.away_conversion_att += 1
    return home_scorekeeper_2(state)

@route
def home_fail_2(state: State) -> Page:
    '''
    after touchdown, updates touchdown conversion data,
    returns other team's scorekeeper
    '''
    state.home_conversion_att += 1
    return away_scorekeeper_2(state)

@route
def away_fail_OT(state: State) -> Page:
    '''
    after touchdown, updates touchdown conversion data,
    returns other team's scorekeeper
    '''
    state.away_conversion_att += 1
    return home_overtime(state)

@route
def home_fail_OT(state: State) -> Page:
    '''
    after touchdown, updates touchdown conversion data,
    returns other team's scorekeeper
    '''
    state.home_conversion_att += 1
    return away_overtime(state)

@route
def away_field_goal_page(state: State) -> Page:
    '''
    presents user with choice of team making or failing field goal, updates field goal attempt count;
    returns other team's scorekeeper
    '''
    state.away_field_goal_att += 1
    return Page(state,[
        "The", state.away_team.name, "are kicking a field goal", "\n",
        change_background_color(Button("Attempt is Good","away_field_goal"),state.away_team.color),
        change_background_color(Button("No Good","home_scorekeeper"),"gray")
        ])

@route
def home_field_goal_page(state: State) -> Page:
    '''
    presents user with choice of team making or failing field goal, updates field goal attempt count;
    returns other team's scorekeeper
    '''
    state.home_field_goal_att += 1
    return Page(state,[
        "The", state.home_team.name, "are kicking a field goal", "\n",
        change_background_color(Button("Attempt is Good","home_field_goal"),state.home_team.color),
        change_background_color(Button("No Good","away_scorekeeper"),"gray")
        ])

@route
def away_field_goal_page_2(state: State) -> Page:
    '''
    presents user with choice of team making or failing field goal, updates field goal attempt count;
    returns other team's scorekeeper
    '''
    state.away_field_goal_att += 1
    return Page(state,[
        "The", state.away_team.name, "are kicking a field goal", "\n",
        change_background_color(Button("Attempt is Good","away_field_goal_2"),state.away_team.color),
        change_background_color(Button("No Good","home_scorekeeper_2"),"gray")
        ])

@route
def home_field_goal_page_2(state: State) -> Page:
    '''
    presents user with choice of team making or failing field goal, updates field goal attempt count;
    returns other team's scorekeeper
    '''
    state.home_field_goal_att += 1
    return Page(state,[
        "The", state.home_team.name, "are kicking a field goal", "\n",
        change_background_color(Button("Attempt is Good","home_field_goal_2"),state.home_team.color),
        change_background_color(Button("No Good","away_scorekeeper_2"),"gray")
        ])

@route
def away_field_goal_page_OT(state: State) -> Page:
    '''
    presents user with choice of team making or failing field goal, updates field goal attempt count;
    returns other team's scorekeeper
    '''
    state.away_field_goal_att += 1
    return Page(state,[
        "The", state.away_team.name, "are kicking a field goal", "\n",
        change_background_color(Button("Attempt is Good","away_field_goal_OT"),state.away_team.color),
        change_background_color(Button("No Good","home_overtime"),"gray")
        ])

@route
def home_field_goal_page_OT(state: State) -> Page:
    '''
    presents user with choice of team making or failing field goal, updates field goal attempt count;
    returns other team's scorekeeper
    '''
    state.home_field_goal_att += 1
    return Page(state,[
        "The", state.home_team.name, "are kicking a field goal", "\n",
        change_background_color(Button("Attempt is Good","home_field_goal_OT"),state.home_team.color),
        change_background_color(Button("No Good","away_overtime"),"gray")
        ])

@route
def away_field_goal(state: State) -> Page:
    '''
    after user selects team to make a field goal, updates field goal data,
    returns other team's scorekeeper
    '''
    state.away_field_goal_made += 1
    state.away_score = state.away_score + 3
    return home_scorekeeper(state)

@route
def home_field_goal(state: State) -> Page:
    '''
    after user selects team to make a field goal, updates field goal data,
    returns other team's scorekeeper
    '''
    state.home_field_goal_made += 1
    state.home_score = state.home_score + 3
    return away_scorekeeper(state)

@route
def away_field_goal_2(state: State) -> Page:
    '''
    after user selects team to make a field goal, updates field goal data,
    returns other team's scorekeeper
    '''
    state.away_field_goal_made += 1
    state.away_score = state.away_score + 3
    return home_scorekeeper_2(state)

@route
def home_field_goal_2(state: State) -> Page:
    '''
    after user selects team to make a field goal, updates field goal data,
    returns other team's scorekeeper
    '''
    state.home_field_goal_made += 1
    state.home_score = state.home_score + 3
    return away_scorekeeper_2(state)

@route
def away_field_goal_OT(state: State) -> Page:
    '''
    after user selects team to make a field goal, updates field goal data,
    returns other team's scorekeeper
    '''
    state.away_field_goal_made += 1
    state.away_score = state.away_score + 3
    return home_overtime(state)

@route
def home_field_goal_OT(state: State) -> Page:
    '''
    after user selects team to make a field goal, updates field goal data,
    returns other team's scorekeeper
    '''
    state.home_field_goal_made += 1
    state.home_score = state.home_score + 3
    return away_overtime(state)

@route
def away_two_points(state: State) -> Page:
    '''
    after touchdown, gives team two points, updates touchdown conversion data,
    returns other team's scorekeeper
    '''
    state.away_score = state.away_score + 2
    state.away_conversion_att += 1
    state.away_conversion_made += 1
    return home_scorekeeper(state)

@route
def home_two_points(state: State) -> Page:
    '''
    after touchdown, gives team two points, updates touchdown conversion data,
    returns other team's scorekeeper
    '''
    state.home_score = state.home_score + 2
    state.home_conversion_att += 1
    state.home_conversion_made += 1
    return away_scorekeeper(state)

@route
def away_two_points_2(state: State) -> Page:
    '''
    after touchdown, gives team two points, updates touchdown conversion data,
    returns other team's scorekeeper
    '''
    state.away_score = state.away_score + 2
    state.away_conversion_att += 1
    state.away_conversion_made += 1
    return home_scorekeeper_2(state)

@route
def home_two_points_2(state: State) -> Page:
    '''
    after touchdown, gives team two points, updates touchdown conversion data,
    returns other team's scorekeeper
    '''
    state.home_score = state.home_score + 2
    state.home_conversion_att += 1
    state.home_conversion_made += 1
    return away_scorekeeper_2(state)

@route
def away_two_points_OT(state: State) -> Page:
    '''
    after touchdown, gives team two points, updates touchdown conversion data,
    returns other team's scorekeeper
    '''
    state.away_score = state.away_score + 2
    state.away_conversion_att += 1
    state.away_conversion_made += 1
    return home_overtime(state)

@route
def home_two_points_OT(state: State) -> Page:
    '''
    after touchdown, gives team two points, updates touchdown conversion data,
    returns other team's scorekeeper
    '''
    state.home_score = state.home_score + 2
    state.home_conversion_att += 1
    state.home_conversion_made += 1
    return away_overtime(state)

@route
def away_safety(state: State) -> Page:
    '''
    awards other team two points and gives them ball
    '''
    state.away_score = state.away_score + 2
    return away_scorekeeper(state)

@route
def home_safety(state: State) -> Page:
    '''
    awards other team two points and gives them ball
    '''
    state.home_score = state.home_score + 2
    return home_scorekeeper(state)

@route
def away_safety_2(state: State) -> Page:
    '''
    awards other team two points and gives them ball
    '''
    state.away_score = state.away_score + 2
    return away_scorekeeper_2(state)

@route
def home_safety_2(state: State) -> Page:
    '''
    awards other team two points and gives them ball
    '''
    state.home_score = state.home_score + 2
    return home_scorekeeper_2(state)

@route
def away_safety_OT(state: State) -> Page:
    '''
    awards other team two points and gives them ball
    '''
    state.away_score = state.away_score + 2
    return away_overtime(state)

@route
def home_safety_OT(state: State) -> Page:
    '''
    awards other team two points and gives them ball
    '''
    state.home_score = state.home_score + 2
    return home_overtime(state)


@route
def away_one_point(state: State) -> Page:
    '''
    after touchdown, awards team 1 point, updates touchdown conversion data;
    gives other team ball
    '''
    state.away_score = state.away_score + 1
    state.away_conversion_att += 1
    state.away_conversion_made += 1
    return home_scorekeeper(state)

@route
def home_one_point(state: State) -> Page:
    '''
    after touchdown, awards team 1 point, updates touchdown conversion data;
    gives other team ball
    '''
    state.home_score = state.home_score + 1
    state.home_conversion_att += 1
    state.home_conversion_made += 1
    return away_scorekeeper(state)

@route
def away_one_point_2(state: State) -> Page:
    '''
    after touchdown, awards team 1 point, updates touchdown conversion data;
    gives other team ball
    '''
    state.away_score = state.away_score + 1
    state.away_conversion_att += 1
    state.away_conversion_made += 1
    return home_scorekeeper_2(state)

@route
def home_one_point_2(state: State) -> Page:
    '''
    after touchdown, awards team 1 point, updates touchdown conversion data;
    gives other team ball
    '''
    state.home_score = state.home_score + 1
    state.home_conversion_att += 1
    state.home_conversion_made += 1
    return away_scorekeeper_2(state)

@route
def away_one_point_OT(state: State) -> Page:
    '''
    after touchdown, awards team 1 point, updates touchdown conversion data;
    gives other team ball
    '''
    state.away_score = state.away_score + 1
    state.away_conversion_att += 1
    state.away_conversion_made += 1
    return home_overtime(state)

@route
def home_one_point_OT(state: State) -> Page:
    '''
    after touchdown, awards team 1 point, updates touchdown conversion data;
    gives other team ball
    '''
    state.home_score = state.home_score + 1
    state.home_conversion_att += 1
    state.home_conversion_made += 1
    return away_overtime(state)

@route
def away_punt(state: State) -> Page:
    '''
    gives ball to the other team and updates the punt count
    '''
    state.away_punt += 1
    return home_scorekeeper(state)

@route
def home_punt(state: State) -> Page:
    '''
    gives ball to the other team and updates the punt count
    '''
    state.home_punt += 1
    return away_scorekeeper(state)

@route
def away_punt_2(state: State) -> Page:
    '''
    gives ball to the other team and updates the punt count
    '''
    state.away_punt += 1
    return home_scorekeeper_2(state)

@route
def home_punt_2(state: State) -> Page:
    '''
    gives ball to the other team and updates the punt count
    '''
    state.home_punt += 1
    return away_scorekeeper_2(state)

@route
def away_punt_OT(state: State) -> Page:
    '''
    gives ball to the other team and updates the punt count
    '''
    state.away_punt += 1
    return home_overtime(state)

@route
def home_punt_OT(state: State) -> Page:
    '''
    gives ball to the other team and updates the punt count
    '''
    state.home_punt += 1
    return away_overtime(state)

@route
def away_turnover(state: State) -> Page:
    '''
    gives ball to the other team, and updates the turnover count
    '''
    state.away_turnover += 1
    return home_scorekeeper(state)

@route
def home_turnover(state: State) -> Page:
    '''
    gives ball to the other team, and updates the turnover count
    '''
    state.home_turnover += 1
    return away_scorekeeper(state)

@route
def away_turnover_2(state: State) -> Page:
    '''
    gives ball to the other team, and updates the turnover count
    '''
    state.away_turnover += 1
    return home_scorekeeper_2(state)

@route
def home_turnover_2(state: State) -> Page:
    '''
    gives ball to the other team, and updates the turnover count
    '''
    state.home_turnover += 1
    return away_scorekeeper_2(state)

@route
def away_turnover_OT(state: State) -> Page:
    '''
    gives ball to the other team, and updates the turnover count
    '''
    state.away_turnover += 1
    return home_overtime(state)

@route
def home_turnover_OT(state: State) -> Page:
    '''
    gives ball to the other team, and updates the turnover count
    '''
    state.home_turnover += 1
    return away_overtime(state)

@route
def away_turnover_on_downs(state: State) -> Page:
    '''
    gives other team the ball, not adding to turnover count
    '''
    return home_scorekeeper(state)

@route
def home_turnover_on_downs(state: State) -> Page:
    '''
    gives other team the ball, not adding to turnover count
    '''
    return away_scorekeeper(state)

@route
def away_turnover_on_downs_2(state: State) -> Page:
    '''
    gives other team the ball, not adding to turnover count
    '''
    return home_scorekeeper_2(state)

@route
def home_turnover_on_downs_2(state: State) -> Page:
    '''
    gives other team the ball, not adding to turnover count
    '''
    return away_scorekeeper_2(state)

@route
def away_turnover_on_downs_OT(state: State) -> Page:
    '''
    gives other team the ball, not adding to turnover count
    '''
    return home_overtime(state)

@route
def home_turnover_on_downs_OT(state: State) -> Page:
    '''
    gives other team the ball, not adding to turnover count
    '''
    return away_overtime(state)

@route
def halftime(state: State) -> Page:
    '''
    displays the game's score at halftime,
    prompts the user to start 2nd half
    '''
    return Page(state,[
        "Halftime Score: ","\n",
        state.away_team.name,": ",state.away_score,"\n",
        state.home_team.name,": ",state.home_score,"\n",
        change_background_color(Button("Start 2nd Half", "second_half_ball"),"gray")
        ])

@route
def second_half_ball(state: State) -> Page:
    '''
    uses the data from the start of the game, when the 'second half team' was designated
    to determine which team gets the ball to start the second half;
    sends user to the score keeper for the 'second half team'
    '''
    if state.second_half_team.name == state.away_team.name:
        return away_scorekeeper_2(state)
    elif state.second_half_team.name == state.home_team.name:
        return home_scorekeeper_2(state)

@route
def overtime_cointoss(state: State) -> Page:
    '''
    allows user to input which team wins the overtime cointoss
    '''
    if state.away_score != state.home_score:
        return final(state)
    else:
        return Page(state,[
            "Select which team starts with the ball for overtime: ","\n",
            change_background_color(Button(state.away_team.name, "away_overtime"),state.away_team.color),
            change_background_color(Button(state.home_team.name, "home_overtime"),state.home_team.color)
            ])

@route
def away_overtime(state: State) -> Page:
    '''
    allows user to update away team's scores in overtime
    '''
    return Page(state,[
        "Overtime!","\n",
        "Current score: ", state.away_team.name, str(state.away_score), "-", str(state.home_score), state.home_team.name, "\n",
        change_background_color(Button("Touchdown", "away_touchdown_OT"), state.away_team.color),
        change_background_color(Button("Field Goal", "away_field_goal_page_OT"), state.away_team.color),
        change_background_color(Button("Punt","away_punt_OT"),state.away_team.color),
        change_background_color(Button("Turnover","away_turnover_OT"),state.away_team.color),
        change_background_color(Button("4th Down Fail","away_turnover_on_downs_OT"),state.away_team.color),
        change_background_color(Button("Safety", "home_safety_OT"), "black"), "\n",
        change_background_color(Button("End Game","final"), "gray")
    ])

@route
def home_overtime(state: State) -> Page:
    '''
    allows user to update home team's scores in overtime
    '''
    return Page(state,[
        "Overtime!","\n",
        "Current score: ", state.away_team.name, str(state.away_score), "-", str(state.home_score), state.home_team.name, "\n",
        change_background_color(Button("Safety", "away_safety_OT"), "black"),
        change_background_color(Button("4th Down Fail","home_turnover_on_downs_OT"),state.home_team.color),
        change_background_color(Button("Turnover","home_turnover_OT"),state.home_team.color),
        change_background_color(Button("Punt","home_punt_OT"),state.home_team.color),
        change_background_color(Button("Field Goal", "home_field_goal_page_OT"), state.home_team.color),
        change_background_color(Button("Touchdown", "home_touchdown_OT"), state.home_team.color),"\n",
        change_background_color(Button("End Game","final"), "gray")
    ])

@route
def final(state: State) -> Page:
    '''
    uses data from the game to create a final score report and a stat sheet;
    takes in all of the state variables,
    returns Page with the data reformatted for viewing
    '''
    Score_list = [state.away_score,state.home_score] #list containing the two scores
    high_scores = [] #contains any score above 30
    low_scores = [] #contains any score below 15
    details = ""
    max_score = Score_list
    for score in Score_list:
        if score > 30:
            high_scores.append(score)
        elif score < 15:
            low_scores.append(score)
    if len(high_scores) == 2:
        details = " in a high-scoring game" #both scores above 30
    elif len(high_scores) == 1:
        if (state.away_score - state.home_score)>20:
            details = " in a blowout" #difference is over 20
        elif (state.home_score-state.away_score)>20:
            details = " in a blowout" #differences is over 20
        else:
            details = ""
    elif len(low_scores) == 2:
        details = " in a defensive match-up" #neither team scored 15 or more
    elif (state.away_score - state.home_score)>20:
        details = " in a blowout" #difference is over 20
    elif (state.home_score-state.away_score)>20:
        details = " in a blowout" #difference is over 20
    win_message = ""
    away_turnover_message = ""
    home_turnoevr_message = ""
    away_punt_message = ""
    home_punt_message = ""
    if state.away_score > state.home_score:
        win_message = "The "+state.away_team.name+" have won"+details+"!"
    elif state.home_score > state.away_score:
        win_message = "The "+state.home_team.name+" have won"+details+"!"
    else:
        win_message = "The "+state.away_team.name+" and the "+state.home_team.name+" have tied "+details
    if state.away_turnover == 1:
        away_turnover_message = "committed "+str(state.away_turnover)+" turnover"
    else:
        away_turnover_message = "commited "+str(state.away_turnover)+" turnovers"
    if state.home_turnover == 1:
        home_turnover_message = "committed "+str(state.home_turnover)+" turnover"
    else:
        home_turnover_message = "commited "+str(state.home_turnover)+" turnovers"
    if state.away_punt == 1:
        away_punt_message = "punted "+str(state.away_punt)+" time,"
    else:
        away_punt_message = "punted "+str(state.away_punt)+" times,"
    if state.home_punt == 1:
        home_punt_message = "punted "+str(state.home_punt)+" time,"
    else:
        home_punt_message = "punted "+str(state.home_punt)+" times,"
    
    return Page(state,[
        win_message,"\n",
        state.away_team.name,": ",state.away_score, "\n",
        "The "+state.away_team.name+" went "+str(state.away_field_goal_made)+"/"+str(state.away_field_goal_att),
        "on field goals, converted "+str(state.away_conversion_made)+"/"+str(state.away_conversion_att)+" of their touchdowns,",
        away_punt_message," and ",away_turnover_message,"\n",
        state.home_team.name,": ",state.home_score, "\n",
        "The "+state.home_team.name+" went "+str(state.home_field_goal_made)+"/"+str(state.home_field_goal_att),
        "on field goals, converted "+str(state.home_conversion_made)+"/"+str(state.home_conversion_att)+" of their touchdowns,",
        home_punt_message," and ",home_turnover_message,"\n",
        change_background_color(Button("New Game","away_team_selection"),"gray"),"\n",
        change_background_color(Button("Home Page","index"),"gray")
        ])
        

# ---------------------------------------------------------------------------
# assert_equal tests
# Each route is called with a fresh sample State. These tests check that every
# route returns a Page and that any state changes made by the route are correct.
# ---------------------------------------------------------------------------
def _test_state() -> State:
    return State(Team("Away", "#111111"), Team("Home", "#222222"),
                 10, 10, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, Team('Away', '#111111'))

_test_index_state = _test_state()
_test_index_result = index(_test_index_state)
assert_equal(type(_test_index_result).__name__, "Page")

_test_away_team_selection_state = _test_state()
_test_away_team_selection_result = away_team_selection(_test_away_team_selection_state)
assert_equal(type(_test_away_team_selection_result).__name__, "Page")
assert_equal(_test_away_team_selection_state.home_score, 0)
assert_equal(_test_away_team_selection_state.away_score, 0)
assert_equal(_test_away_team_selection_state.away_field_goal_att, 0)
assert_equal(_test_away_team_selection_state.away_field_goal_made, 0)
assert_equal(_test_away_team_selection_state.home_field_goal_att, 0)
assert_equal(_test_away_team_selection_state.home_field_goal_made, 0)
assert_equal(_test_away_team_selection_state.away_conversion_att, 0)
assert_equal(_test_away_team_selection_state.away_conversion_made, 0)
assert_equal(_test_away_team_selection_state.home_conversion_att, 0)
assert_equal(_test_away_team_selection_state.home_conversion_made, 0)
assert_equal(_test_away_team_selection_state.away_punt, 0)
assert_equal(_test_away_team_selection_state.home_punt, 0)
assert_equal(_test_away_team_selection_state.away_turnover, 0)
assert_equal(_test_away_team_selection_state.home_turnover, 0)

_test_home_team_selection_state = _test_state()
_test_home_team_selection_result = home_team_selection(_test_home_team_selection_state)
assert_equal(type(_test_home_team_selection_result).__name__, "Page")

_test_custom_away_state = _test_state()
_test_custom_away_result = custom_away(_test_custom_away_state)
assert_equal(type(_test_custom_away_result).__name__, "Page")

_test_away_hexcode_page_state = _test_state()
_test_away_hexcode_page_result = away_hexcode_page(_test_away_hexcode_page_state)
assert_equal(type(_test_away_hexcode_page_result).__name__, "Page")

_test_custom_away_submit_state = _test_state()
_test_custom_away_submit_result = custom_away_submit(_test_custom_away_submit_state, "Custom Away", "#abcdef")
assert_equal(type(_test_custom_away_submit_result).__name__, "Page")

_test_custom_home_state = _test_state()
_test_custom_home_result = custom_home(_test_custom_home_state)
assert_equal(type(_test_custom_home_result).__name__, "Page")

_test_home_hexcode_page_state = _test_state()
_test_home_hexcode_page_result = home_hexcode_page(_test_home_hexcode_page_state)
assert_equal(type(_test_home_hexcode_page_result).__name__, "Page")

_test_custom_home_submit_state = _test_state()
_test_custom_home_submit_result = custom_home_submit(_test_custom_home_submit_state, "Custom Home", "#fedcba")
assert_equal(type(_test_custom_home_submit_result).__name__, "Page")

_test_back_state = _test_state()
_test_back_result = back(_test_back_state)
assert_equal(type(_test_back_result).__name__, "Page")

_test_nfc_east_state = _test_state()
_test_nfc_east_result = nfc_east(_test_nfc_east_state)
assert_equal(type(_test_nfc_east_result).__name__, "Page")

_test_eagles_state = _test_state()
_test_eagles_result = eagles(_test_eagles_state)
assert_equal(type(_test_eagles_result).__name__, "Page")
assert_equal(_test_eagles_state.away_team.name, 'Eagles')
assert_equal(_test_eagles_state.away_team.color, '#004953')

_test_cowboys_state = _test_state()
_test_cowboys_result = cowboys(_test_cowboys_state)
assert_equal(type(_test_cowboys_result).__name__, "Page")
assert_equal(_test_cowboys_state.away_team.name, 'Cowboys')
assert_equal(_test_cowboys_state.away_team.color, '#003594')

_test_giants_state = _test_state()
_test_giants_result = giants(_test_giants_state)
assert_equal(type(_test_giants_result).__name__, "Page")
assert_equal(_test_giants_state.away_team.name, 'Giants')
assert_equal(_test_giants_state.away_team.color, '#0b2265')

_test_commanders_state = _test_state()
_test_commanders_result = commanders(_test_commanders_state)
assert_equal(type(_test_commanders_result).__name__, "Page")
assert_equal(_test_commanders_state.away_team.name, 'Commanders')
assert_equal(_test_commanders_state.away_team.color, '#5a1414')

_test_nfc_south_state = _test_state()
_test_nfc_south_result = nfc_south(_test_nfc_south_state)
assert_equal(type(_test_nfc_south_result).__name__, "Page")

_test_panthers_state = _test_state()
_test_panthers_result = panthers(_test_panthers_state)
assert_equal(type(_test_panthers_result).__name__, "Page")
assert_equal(_test_panthers_state.away_team.name, 'Panthers')
assert_equal(_test_panthers_state.away_team.color, '#0085ca')

_test_falcons_state = _test_state()
_test_falcons_result = falcons(_test_falcons_state)
assert_equal(type(_test_falcons_result).__name__, "Page")
assert_equal(_test_falcons_state.away_team.name, 'Falcons')
assert_equal(_test_falcons_state.away_team.color, '#a71930')

_test_saints_state = _test_state()
_test_saints_result = saints(_test_saints_state)
assert_equal(type(_test_saints_result).__name__, "Page")
assert_equal(_test_saints_state.away_team.name, 'Saints')
assert_equal(_test_saints_state.away_team.color, '#d3bc8d')

_test_buccaneers_state = _test_state()
_test_buccaneers_result = buccaneers(_test_buccaneers_state)
assert_equal(type(_test_buccaneers_result).__name__, "Page")
assert_equal(_test_buccaneers_state.away_team.name, 'Buccaneers')
assert_equal(_test_buccaneers_state.away_team.color, '#d50a0a')

_test_nfc_west_state = _test_state()
_test_nfc_west_result = nfc_west(_test_nfc_west_state)
assert_equal(type(_test_nfc_west_result).__name__, "Page")

_test_rams_state = _test_state()
_test_rams_result = rams(_test_rams_state)
assert_equal(type(_test_rams_result).__name__, "Page")
assert_equal(_test_rams_state.away_team.name, 'Rams')
assert_equal(_test_rams_state.away_team.color, '#003594')

_test_seahawks_state = _test_state()
_test_seahawks_result = seahawks(_test_seahawks_state)
assert_equal(type(_test_seahawks_result).__name__, "Page")
assert_equal(_test_seahawks_state.away_team.name, 'Seahawks')
assert_equal(_test_seahawks_state.away_team.color, '#69be28')

_test_fortyniners_state = _test_state()
_test_fortyniners_result = fortyniners(_test_fortyniners_state)
assert_equal(type(_test_fortyniners_result).__name__, "Page")
assert_equal(_test_fortyniners_state.away_team.name, 'Forty-Niners')
assert_equal(_test_fortyniners_state.away_team.color, '#b3995d')

_test_cardinals_state = _test_state()
_test_cardinals_result = cardinals(_test_cardinals_state)
assert_equal(type(_test_cardinals_result).__name__, "Page")
assert_equal(_test_cardinals_state.away_team.name, 'Cardinals')
assert_equal(_test_cardinals_state.away_team.color, '#97233f')

_test_nfc_north_state = _test_state()
_test_nfc_north_result = nfc_north(_test_nfc_north_state)
assert_equal(type(_test_nfc_north_result).__name__, "Page")

_test_lions_state = _test_state()
_test_lions_result = lions(_test_lions_state)
assert_equal(type(_test_lions_result).__name__, "Page")
assert_equal(_test_lions_state.away_team.name, 'Lions')
assert_equal(_test_lions_state.away_team.color, '#0076b6')

_test_packers_state = _test_state()
_test_packers_result = packers(_test_packers_state)
assert_equal(type(_test_packers_result).__name__, "Page")
assert_equal(_test_packers_state.away_team.name, 'Packers')
assert_equal(_test_packers_state.away_team.color, '#203731')

_test_bears_state = _test_state()
_test_bears_result = bears(_test_bears_state)
assert_equal(type(_test_bears_result).__name__, "Page")
assert_equal(_test_bears_state.away_team.name, 'Bears')
assert_equal(_test_bears_state.away_team.color, '#c83803')

_test_vikings_state = _test_state()
_test_vikings_result = vikings(_test_vikings_state)
assert_equal(type(_test_vikings_result).__name__, "Page")
assert_equal(_test_vikings_state.away_team.name, 'Vikings')
assert_equal(_test_vikings_state.away_team.color, '#4f2683')

_test_afc_east_state = _test_state()
_test_afc_east_result = afc_east(_test_afc_east_state)
assert_equal(type(_test_afc_east_result).__name__, "Page")

_test_patriots_state = _test_state()
_test_patriots_result = patriots(_test_patriots_state)
assert_equal(type(_test_patriots_result).__name__, "Page")
assert_equal(_test_patriots_state.away_team.name, 'Patriots')
assert_equal(_test_patriots_state.away_team.color, '#002244')

_test_bills_state = _test_state()
_test_bills_result = bills(_test_bills_state)
assert_equal(type(_test_bills_result).__name__, "Page")
assert_equal(_test_bills_state.away_team.name, 'Bills')
assert_equal(_test_bills_state.away_team.color, '#c60c30')

_test_jets_state = _test_state()
_test_jets_result = jets(_test_jets_state)
assert_equal(type(_test_jets_result).__name__, "Page")
assert_equal(_test_jets_state.away_team.name, 'Jets')
assert_equal(_test_jets_state.away_team.color, '#125740')

_test_dolphins_state = _test_state()
_test_dolphins_result = dolphins(_test_dolphins_state)
assert_equal(type(_test_dolphins_result).__name__, "Page")
assert_equal(_test_dolphins_state.away_team.name, 'Dolphins')
assert_equal(_test_dolphins_state.away_team.color, '#008e97')

_test_afc_south_state = _test_state()
_test_afc_south_result = afc_south(_test_afc_south_state)
assert_equal(type(_test_afc_south_result).__name__, "Page")

_test_jaguars_state = _test_state()
_test_jaguars_result = jaguars(_test_jaguars_state)
assert_equal(type(_test_jaguars_result).__name__, "Page")
assert_equal(_test_jaguars_state.away_team.name, 'Jaguars')
assert_equal(_test_jaguars_state.away_team.color, '#006778')

_test_texans_state = _test_state()
_test_texans_result = texans(_test_texans_state)
assert_equal(type(_test_texans_result).__name__, "Page")
assert_equal(_test_texans_state.away_team.name, 'Texans')
assert_equal(_test_texans_state.away_team.color, '#03202f')

_test_titans_state = _test_state()
_test_titans_result = titans(_test_titans_state)
assert_equal(type(_test_titans_result).__name__, "Page")
assert_equal(_test_titans_state.away_team.name, 'Titans')
assert_equal(_test_titans_state.away_team.color, '#4b92db')

_test_colts_state = _test_state()
_test_colts_result = colts(_test_colts_state)
assert_equal(type(_test_colts_result).__name__, "Page")
assert_equal(_test_colts_state.away_team.name, 'Colts')
assert_equal(_test_colts_state.away_team.color, '#002c5f')

_test_afc_west_state = _test_state()
_test_afc_west_result = afc_west(_test_afc_west_state)
assert_equal(type(_test_afc_west_result).__name__, "Page")

_test_broncos_state = _test_state()
_test_broncos_result = broncos(_test_broncos_state)
assert_equal(type(_test_broncos_result).__name__, "Page")
assert_equal(_test_broncos_state.away_team.name, 'Broncos')
assert_equal(_test_broncos_state.away_team.color, '#fb1414')

_test_chiefs_state = _test_state()
_test_chiefs_result = chiefs(_test_chiefs_state)
assert_equal(type(_test_chiefs_result).__name__, "Page")
assert_equal(_test_chiefs_state.away_team.name, 'Chiefs')
assert_equal(_test_chiefs_state.away_team.color, '#e31837')

_test_raiders_state = _test_state()
_test_raiders_result = raiders(_test_raiders_state)
assert_equal(type(_test_raiders_result).__name__, "Page")
assert_equal(_test_raiders_state.away_team.name, 'Raiders')
assert_equal(_test_raiders_state.away_team.color, '#a5acaf')

_test_chargers_state = _test_state()
_test_chargers_result = chargers(_test_chargers_state)
assert_equal(type(_test_chargers_result).__name__, "Page")
assert_equal(_test_chargers_state.away_team.name, 'Chargers')
assert_equal(_test_chargers_state.away_team.color, '#0080c6')

_test_afc_north_state = _test_state()
_test_afc_north_result = afc_north(_test_afc_north_state)
assert_equal(type(_test_afc_north_result).__name__, "Page")

_test_ravens_state = _test_state()
_test_ravens_result = ravens(_test_ravens_state)
assert_equal(type(_test_ravens_result).__name__, "Page")
assert_equal(_test_ravens_state.away_team.name, 'Ravens')
assert_equal(_test_ravens_state.away_team.color, '#241773')

_test_steelers_state = _test_state()
_test_steelers_result = steelers(_test_steelers_state)
assert_equal(type(_test_steelers_result).__name__, "Page")
assert_equal(_test_steelers_state.away_team.name, 'Steelers')
assert_equal(_test_steelers_state.away_team.color, '#ffb612')

_test_browns_state = _test_state()
_test_browns_result = browns(_test_browns_state)
assert_equal(type(_test_browns_result).__name__, "Page")
assert_equal(_test_browns_state.away_team.name, 'Browns')
assert_equal(_test_browns_state.away_team.color, '#331d00')

_test_bengals_state = _test_state()
_test_bengals_result = bengals(_test_bengals_state)
assert_equal(type(_test_bengals_result).__name__, "Page")
assert_equal(_test_bengals_state.away_team.name, 'Bengals')
assert_equal(_test_bengals_state.away_team.color, '#fb1414')

_test_back2_state = _test_state()
_test_back2_result = back2(_test_back2_state)
assert_equal(type(_test_back2_result).__name__, "Page")

_test_nfc_east2_state = _test_state()
_test_nfc_east2_result = nfc_east2(_test_nfc_east2_state)
assert_equal(type(_test_nfc_east2_result).__name__, "Page")

_test_eagles2_state = _test_state()
_test_eagles2_result = eagles2(_test_eagles2_state)
assert_equal(type(_test_eagles2_result).__name__, "Page")
assert_equal(_test_eagles2_state.home_team.name, 'Eagles')
assert_equal(_test_eagles2_state.home_team.color, '#004953')

_test_cowboys2_state = _test_state()
_test_cowboys2_result = cowboys2(_test_cowboys2_state)
assert_equal(type(_test_cowboys2_result).__name__, "Page")
assert_equal(_test_cowboys2_state.home_team.name, 'Cowboys')
assert_equal(_test_cowboys2_state.home_team.color, '#003594')

_test_giants2_state = _test_state()
_test_giants2_result = giants2(_test_giants2_state)
assert_equal(type(_test_giants2_result).__name__, "Page")
assert_equal(_test_giants2_state.home_team.name, 'Giants')
assert_equal(_test_giants2_state.home_team.color, '#0b2265')

_test_commanders2_state = _test_state()
_test_commanders2_result = commanders2(_test_commanders2_state)
assert_equal(type(_test_commanders2_result).__name__, "Page")
assert_equal(_test_commanders2_state.home_team.name, 'Commanders')
assert_equal(_test_commanders2_state.home_team.color, '#5a1414')

_test_nfc_south2_state = _test_state()
_test_nfc_south2_result = nfc_south2(_test_nfc_south2_state)
assert_equal(type(_test_nfc_south2_result).__name__, "Page")

_test_panthers2_state = _test_state()
_test_panthers2_result = panthers2(_test_panthers2_state)
assert_equal(type(_test_panthers2_result).__name__, "Page")
assert_equal(_test_panthers2_state.home_team.name, 'Panthers')
assert_equal(_test_panthers2_state.home_team.color, '#0085ca')

_test_falcons2_state = _test_state()
_test_falcons2_result = falcons2(_test_falcons2_state)
assert_equal(type(_test_falcons2_result).__name__, "Page")
assert_equal(_test_falcons2_state.home_team.name, 'Falcons')
assert_equal(_test_falcons2_state.home_team.color, '#a71930')

_test_saints2_state = _test_state()
_test_saints2_result = saints2(_test_saints2_state)
assert_equal(type(_test_saints2_result).__name__, "Page")
assert_equal(_test_saints2_state.home_team.name, 'Saints')
assert_equal(_test_saints2_state.home_team.color, '#d3bc8d')

_test_buccaneers2_state = _test_state()
_test_buccaneers2_result = buccaneers2(_test_buccaneers2_state)
assert_equal(type(_test_buccaneers2_result).__name__, "Page")
assert_equal(_test_buccaneers2_state.home_team.name, 'Buccaneers')
assert_equal(_test_buccaneers2_state.home_team.color, '#d50a0a')

_test_nfc_west2_state = _test_state()
_test_nfc_west2_result = nfc_west2(_test_nfc_west2_state)
assert_equal(type(_test_nfc_west2_result).__name__, "Page")

_test_rams2_state = _test_state()
_test_rams2_result = rams2(_test_rams2_state)
assert_equal(type(_test_rams2_result).__name__, "Page")
assert_equal(_test_rams2_state.home_team.name, 'Rams')
assert_equal(_test_rams2_state.home_team.color, '#003594')

_test_seahawks2_state = _test_state()
_test_seahawks2_result = seahawks2(_test_seahawks2_state)
assert_equal(type(_test_seahawks2_result).__name__, "Page")
assert_equal(_test_seahawks2_state.home_team.name, 'Seahawks')
assert_equal(_test_seahawks2_state.home_team.color, '#69be28')

_test_fortyniners2_state = _test_state()
_test_fortyniners2_result = fortyniners2(_test_fortyniners2_state)
assert_equal(type(_test_fortyniners2_result).__name__, "Page")
assert_equal(_test_fortyniners2_state.home_team.name, 'Forty-Niners')
assert_equal(_test_fortyniners2_state.home_team.color, '#b3995d')

_test_cardinals2_state = _test_state()
_test_cardinals2_result = cardinals2(_test_cardinals2_state)
assert_equal(type(_test_cardinals2_result).__name__, "Page")
assert_equal(_test_cardinals2_state.home_team.name, 'Cardinals')
assert_equal(_test_cardinals2_state.home_team.color, '#97233f')

_test_nfc_north2_state = _test_state()
_test_nfc_north2_result = nfc_north2(_test_nfc_north2_state)
assert_equal(type(_test_nfc_north2_result).__name__, "Page")

_test_lions2_state = _test_state()
_test_lions2_result = lions2(_test_lions2_state)
assert_equal(type(_test_lions2_result).__name__, "Page")
assert_equal(_test_lions2_state.home_team.name, 'Lions')
assert_equal(_test_lions2_state.home_team.color, '#0076b6')

_test_packers2_state = _test_state()
_test_packers2_result = packers2(_test_packers2_state)
assert_equal(type(_test_packers2_result).__name__, "Page")
assert_equal(_test_packers2_state.home_team.name, 'Packers')
assert_equal(_test_packers2_state.home_team.color, '#203731')

_test_bears2_state = _test_state()
_test_bears2_result = bears2(_test_bears2_state)
assert_equal(type(_test_bears2_result).__name__, "Page")
assert_equal(_test_bears2_state.home_team.name, 'Bears')
assert_equal(_test_bears2_state.home_team.color, '#c83803')

_test_vikings2_state = _test_state()
_test_vikings2_result = vikings2(_test_vikings2_state)
assert_equal(type(_test_vikings2_result).__name__, "Page")
assert_equal(_test_vikings2_state.home_team.name, 'Vikings')
assert_equal(_test_vikings2_state.home_team.color, '#4f2683')

_test_afc_east2_state = _test_state()
_test_afc_east2_result = afc_east2(_test_afc_east2_state)
assert_equal(type(_test_afc_east2_result).__name__, "Page")

_test_patriots2_state = _test_state()
_test_patriots2_result = patriots2(_test_patriots2_state)
assert_equal(type(_test_patriots2_result).__name__, "Page")
assert_equal(_test_patriots2_state.home_team.name, 'Patriots')
assert_equal(_test_patriots2_state.home_team.color, '#002244')

_test_bills2_state = _test_state()
_test_bills2_result = bills2(_test_bills2_state)
assert_equal(type(_test_bills2_result).__name__, "Page")
assert_equal(_test_bills2_state.home_team.name, 'Bills')
assert_equal(_test_bills2_state.home_team.color, '#c60c30')

_test_jets2_state = _test_state()
_test_jets2_result = jets2(_test_jets2_state)
assert_equal(type(_test_jets2_result).__name__, "Page")
assert_equal(_test_jets2_state.home_team.name, 'Jets')
assert_equal(_test_jets2_state.home_team.color, '#125740')

_test_dolphins2_state = _test_state()
_test_dolphins2_result = dolphins2(_test_dolphins2_state)
assert_equal(type(_test_dolphins2_result).__name__, "Page")
assert_equal(_test_dolphins2_state.home_team.name, 'Dolphins')
assert_equal(_test_dolphins2_state.home_team.color, '#008e97')

_test_afc_south2_state = _test_state()
_test_afc_south2_result = afc_south2(_test_afc_south2_state)
assert_equal(type(_test_afc_south2_result).__name__, "Page")

_test_jaguars2_state = _test_state()
_test_jaguars2_result = jaguars2(_test_jaguars2_state)
assert_equal(type(_test_jaguars2_result).__name__, "Page")
assert_equal(_test_jaguars2_state.home_team.name, 'Jaguars')
assert_equal(_test_jaguars2_state.home_team.color, '#006778')

_test_texans2_state = _test_state()
_test_texans2_result = texans2(_test_texans2_state)
assert_equal(type(_test_texans2_result).__name__, "Page")
assert_equal(_test_texans2_state.home_team.name, 'Texans')
assert_equal(_test_texans2_state.home_team.color, '#03202f')

_test_titans2_state = _test_state()
_test_titans2_result = titans2(_test_titans2_state)
assert_equal(type(_test_titans2_result).__name__, "Page")
assert_equal(_test_titans2_state.home_team.name, 'Titans')
assert_equal(_test_titans2_state.home_team.color, '#4b92db')

_test_colts2_state = _test_state()
_test_colts2_result = colts2(_test_colts2_state)
assert_equal(type(_test_colts2_result).__name__, "Page")
assert_equal(_test_colts2_state.home_team.name, 'Colts')
assert_equal(_test_colts2_state.home_team.color, '#002c5f')

_test_afc_west2_state = _test_state()
_test_afc_west2_result = afc_west2(_test_afc_west2_state)
assert_equal(type(_test_afc_west2_result).__name__, "Page")

_test_broncos2_state = _test_state()
_test_broncos2_result = broncos2(_test_broncos2_state)
assert_equal(type(_test_broncos2_result).__name__, "Page")
assert_equal(_test_broncos2_state.home_team.name, 'Broncos')
assert_equal(_test_broncos2_state.home_team.color, '#fb1414')

_test_chiefs2_state = _test_state()
_test_chiefs2_result = chiefs2(_test_chiefs2_state)
assert_equal(type(_test_chiefs2_result).__name__, "Page")
assert_equal(_test_chiefs2_state.home_team.name, 'Chiefs')
assert_equal(_test_chiefs2_state.home_team.color, '#e31837')

_test_raiders2_state = _test_state()
_test_raiders2_result = raiders2(_test_raiders2_state)
assert_equal(type(_test_raiders2_result).__name__, "Page")
assert_equal(_test_raiders2_state.home_team.name, 'Raiders')
assert_equal(_test_raiders2_state.home_team.color, '#a5acaf')

_test_chargers2_state = _test_state()
_test_chargers2_result = chargers2(_test_chargers2_state)
assert_equal(type(_test_chargers2_result).__name__, "Page")
assert_equal(_test_chargers2_state.home_team.name, 'Chargers')
assert_equal(_test_chargers2_state.home_team.color, '#0080c6')

_test_afc_north2_state = _test_state()
_test_afc_north2_result = afc_north2(_test_afc_north2_state)
assert_equal(type(_test_afc_north2_result).__name__, "Page")

_test_ravens2_state = _test_state()
_test_ravens2_result = ravens2(_test_ravens2_state)
assert_equal(type(_test_ravens2_result).__name__, "Page")
assert_equal(_test_ravens2_state.home_team.name, 'Ravens')
assert_equal(_test_ravens2_state.home_team.color, '#241773')

_test_steelers2_state = _test_state()
_test_steelers2_result = steelers2(_test_steelers2_state)
assert_equal(type(_test_steelers2_result).__name__, "Page")
assert_equal(_test_steelers2_state.home_team.name, 'Steelers')
assert_equal(_test_steelers2_state.home_team.color, '#ffb612')

_test_browns2_state = _test_state()
_test_browns2_result = browns2(_test_browns2_state)
assert_equal(type(_test_browns2_result).__name__, "Page")
assert_equal(_test_browns2_state.home_team.name, 'Browns')
assert_equal(_test_browns2_state.home_team.color, '#331d00')

_test_bengals2_state = _test_state()
_test_bengals2_result = bengals2(_test_bengals2_state)
assert_equal(type(_test_bengals2_result).__name__, "Page")
assert_equal(_test_bengals2_state.home_team.name, 'Bengals')
assert_equal(_test_bengals2_state.home_team.color, '#fb1414')

_test_cointoss_state = _test_state()
_test_cointoss_result = cointoss(_test_cointoss_state)
assert_equal(type(_test_cointoss_result).__name__, "Page")

_test_away_team_starts_state = _test_state()
_test_away_team_starts_result = away_team_starts(_test_away_team_starts_state)
assert_equal(type(_test_away_team_starts_result).__name__, "Page")

_test_home_team_starts_state = _test_state()
_test_home_team_starts_result = home_team_starts(_test_home_team_starts_state)
assert_equal(type(_test_home_team_starts_result).__name__, "Page")

_test_away_scorekeeper_state = _test_state()
_test_away_scorekeeper_result = away_scorekeeper(_test_away_scorekeeper_state)
assert_equal(type(_test_away_scorekeeper_result).__name__, "Page")

_test_home_scorekeeper_state = _test_state()
_test_home_scorekeeper_result = home_scorekeeper(_test_home_scorekeeper_state)
assert_equal(type(_test_home_scorekeeper_result).__name__, "Page")

_test_away_scorekeeper_2_state = _test_state()
_test_away_scorekeeper_2_result = away_scorekeeper_2(_test_away_scorekeeper_2_state)
assert_equal(type(_test_away_scorekeeper_2_result).__name__, "Page")

_test_home_scorekeeper_2_state = _test_state()
_test_home_scorekeeper_2_result = home_scorekeeper_2(_test_home_scorekeeper_2_state)
assert_equal(type(_test_home_scorekeeper_2_result).__name__, "Page")

_test_away_touchdown_state = _test_state()
_test_away_touchdown_result = away_touchdown(_test_away_touchdown_state)
assert_equal(type(_test_away_touchdown_result).__name__, "Page")
assert_equal(_test_away_touchdown_state.away_score, 16)

_test_home_touchdown_state = _test_state()
_test_home_touchdown_result = home_touchdown(_test_home_touchdown_state)
assert_equal(type(_test_home_touchdown_result).__name__, "Page")
assert_equal(_test_home_touchdown_state.home_score, 16)

_test_away_touchdown_2_state = _test_state()
_test_away_touchdown_2_result = away_touchdown_2(_test_away_touchdown_2_state)
assert_equal(type(_test_away_touchdown_2_result).__name__, "Page")
assert_equal(_test_away_touchdown_2_state.away_score, 16)

_test_home_touchdown_2_state = _test_state()
_test_home_touchdown_2_result = home_touchdown_2(_test_home_touchdown_2_state)
assert_equal(type(_test_home_touchdown_2_result).__name__, "Page")
assert_equal(_test_home_touchdown_2_state.home_score, 16)

_test_away_touchdown_OT_state = _test_state()
_test_away_touchdown_OT_result = away_touchdown_OT(_test_away_touchdown_OT_state)
assert_equal(type(_test_away_touchdown_OT_result).__name__, "Page")
assert_equal(_test_away_touchdown_OT_state.away_score, 16)

_test_home_touchdown_OT_state = _test_state()
_test_home_touchdown_OT_result = home_touchdown_OT(_test_home_touchdown_OT_state)
assert_equal(type(_test_home_touchdown_OT_result).__name__, "Page")
assert_equal(_test_home_touchdown_OT_state.home_score, 16)

_test_away_fail_state = _test_state()
_test_away_fail_result = away_fail(_test_away_fail_state)
assert_equal(type(_test_away_fail_result).__name__, "Page")
assert_equal(_test_away_fail_state.away_conversion_att, 3)

_test_home_fail_state = _test_state()
_test_home_fail_result = home_fail(_test_home_fail_state)
assert_equal(type(_test_home_fail_result).__name__, "Page")
assert_equal(_test_home_fail_state.home_conversion_att, 3)

_test_away_fail_2_state = _test_state()
_test_away_fail_2_result = away_fail_2(_test_away_fail_2_state)
assert_equal(type(_test_away_fail_2_result).__name__, "Page")
assert_equal(_test_away_fail_2_state.away_conversion_att, 3)

_test_home_fail_2_state = _test_state()
_test_home_fail_2_result = home_fail_2(_test_home_fail_2_state)
assert_equal(type(_test_home_fail_2_result).__name__, "Page")
assert_equal(_test_home_fail_2_state.home_conversion_att, 3)

_test_away_fail_OT_state = _test_state()
_test_away_fail_OT_result = away_fail_OT(_test_away_fail_OT_state)
assert_equal(type(_test_away_fail_OT_result).__name__, "Page")
assert_equal(_test_away_fail_OT_state.away_conversion_att, 3)

_test_home_fail_OT_state = _test_state()
_test_home_fail_OT_result = home_fail_OT(_test_home_fail_OT_state)
assert_equal(type(_test_home_fail_OT_result).__name__, "Page")
assert_equal(_test_home_fail_OT_state.home_conversion_att, 3)

_test_away_field_goal_page_state = _test_state()
_test_away_field_goal_page_result = away_field_goal_page(_test_away_field_goal_page_state)
assert_equal(type(_test_away_field_goal_page_result).__name__, "Page")
assert_equal(_test_away_field_goal_page_state.away_field_goal_att, 3)

_test_home_field_goal_page_state = _test_state()
_test_home_field_goal_page_result = home_field_goal_page(_test_home_field_goal_page_state)
assert_equal(type(_test_home_field_goal_page_result).__name__, "Page")
assert_equal(_test_home_field_goal_page_state.home_field_goal_att, 3)

_test_away_field_goal_page_2_state = _test_state()
_test_away_field_goal_page_2_result = away_field_goal_page_2(_test_away_field_goal_page_2_state)
assert_equal(type(_test_away_field_goal_page_2_result).__name__, "Page")
assert_equal(_test_away_field_goal_page_2_state.away_field_goal_att, 3)

_test_home_field_goal_page_2_state = _test_state()
_test_home_field_goal_page_2_result = home_field_goal_page_2(_test_home_field_goal_page_2_state)
assert_equal(type(_test_home_field_goal_page_2_result).__name__, "Page")
assert_equal(_test_home_field_goal_page_2_state.home_field_goal_att, 3)

_test_away_field_goal_page_OT_state = _test_state()
_test_away_field_goal_page_OT_result = away_field_goal_page_OT(_test_away_field_goal_page_OT_state)
assert_equal(type(_test_away_field_goal_page_OT_result).__name__, "Page")
assert_equal(_test_away_field_goal_page_OT_state.away_field_goal_att, 3)

_test_home_field_goal_page_OT_state = _test_state()
_test_home_field_goal_page_OT_result = home_field_goal_page_OT(_test_home_field_goal_page_OT_state)
assert_equal(type(_test_home_field_goal_page_OT_result).__name__, "Page")
assert_equal(_test_home_field_goal_page_OT_state.home_field_goal_att, 3)

_test_away_field_goal_state = _test_state()
_test_away_field_goal_result = away_field_goal(_test_away_field_goal_state)
assert_equal(type(_test_away_field_goal_result).__name__, "Page")
assert_equal(_test_away_field_goal_state.away_field_goal_made, 2)
assert_equal(_test_away_field_goal_state.away_score, 13)

_test_home_field_goal_state = _test_state()
_test_home_field_goal_result = home_field_goal(_test_home_field_goal_state)
assert_equal(type(_test_home_field_goal_result).__name__, "Page")
assert_equal(_test_home_field_goal_state.home_field_goal_made, 2)
assert_equal(_test_home_field_goal_state.home_score, 13)

_test_away_field_goal_2_state = _test_state()
_test_away_field_goal_2_result = away_field_goal_2(_test_away_field_goal_2_state)
assert_equal(type(_test_away_field_goal_2_result).__name__, "Page")
assert_equal(_test_away_field_goal_2_state.away_field_goal_made, 2)
assert_equal(_test_away_field_goal_2_state.away_score, 13)

_test_home_field_goal_2_state = _test_state()
_test_home_field_goal_2_result = home_field_goal_2(_test_home_field_goal_2_state)
assert_equal(type(_test_home_field_goal_2_result).__name__, "Page")
assert_equal(_test_home_field_goal_2_state.home_field_goal_made, 2)
assert_equal(_test_home_field_goal_2_state.home_score, 13)

_test_away_field_goal_OT_state = _test_state()
_test_away_field_goal_OT_result = away_field_goal_OT(_test_away_field_goal_OT_state)
assert_equal(type(_test_away_field_goal_OT_result).__name__, "Page")
assert_equal(_test_away_field_goal_OT_state.away_field_goal_made, 2)
assert_equal(_test_away_field_goal_OT_state.away_score, 13)

_test_home_field_goal_OT_state = _test_state()
_test_home_field_goal_OT_result = home_field_goal_OT(_test_home_field_goal_OT_state)
assert_equal(type(_test_home_field_goal_OT_result).__name__, "Page")
assert_equal(_test_home_field_goal_OT_state.home_field_goal_made, 2)
assert_equal(_test_home_field_goal_OT_state.home_score, 13)

_test_away_two_points_state = _test_state()
_test_away_two_points_result = away_two_points(_test_away_two_points_state)
assert_equal(type(_test_away_two_points_result).__name__, "Page")
assert_equal(_test_away_two_points_state.away_score, 12)
assert_equal(_test_away_two_points_state.away_conversion_att, 3)
assert_equal(_test_away_two_points_state.away_conversion_made, 2)

_test_home_two_points_state = _test_state()
_test_home_two_points_result = home_two_points(_test_home_two_points_state)
assert_equal(type(_test_home_two_points_result).__name__, "Page")
assert_equal(_test_home_two_points_state.home_score, 12)
assert_equal(_test_home_two_points_state.home_conversion_att, 3)
assert_equal(_test_home_two_points_state.home_conversion_made, 2)

_test_away_two_points_2_state = _test_state()
_test_away_two_points_2_result = away_two_points_2(_test_away_two_points_2_state)
assert_equal(type(_test_away_two_points_2_result).__name__, "Page")
assert_equal(_test_away_two_points_2_state.away_score, 12)
assert_equal(_test_away_two_points_2_state.away_conversion_att, 3)
assert_equal(_test_away_two_points_2_state.away_conversion_made, 2)

_test_home_two_points_2_state = _test_state()
_test_home_two_points_2_result = home_two_points_2(_test_home_two_points_2_state)
assert_equal(type(_test_home_two_points_2_result).__name__, "Page")
assert_equal(_test_home_two_points_2_state.home_score, 12)
assert_equal(_test_home_two_points_2_state.home_conversion_att, 3)
assert_equal(_test_home_two_points_2_state.home_conversion_made, 2)

_test_away_two_points_OT_state = _test_state()
_test_away_two_points_OT_result = away_two_points_OT(_test_away_two_points_OT_state)
assert_equal(type(_test_away_two_points_OT_result).__name__, "Page")
assert_equal(_test_away_two_points_OT_state.away_score, 12)
assert_equal(_test_away_two_points_OT_state.away_conversion_att, 3)
assert_equal(_test_away_two_points_OT_state.away_conversion_made, 2)

_test_home_two_points_OT_state = _test_state()
_test_home_two_points_OT_result = home_two_points_OT(_test_home_two_points_OT_state)
assert_equal(type(_test_home_two_points_OT_result).__name__, "Page")
assert_equal(_test_home_two_points_OT_state.home_score, 12)
assert_equal(_test_home_two_points_OT_state.home_conversion_att, 3)
assert_equal(_test_home_two_points_OT_state.home_conversion_made, 2)

_test_away_safety_state = _test_state()
_test_away_safety_result = away_safety(_test_away_safety_state)
assert_equal(type(_test_away_safety_result).__name__, "Page")
assert_equal(_test_away_safety_state.away_score, 12)

_test_home_safety_state = _test_state()
_test_home_safety_result = home_safety(_test_home_safety_state)
assert_equal(type(_test_home_safety_result).__name__, "Page")
assert_equal(_test_home_safety_state.home_score, 12)

_test_away_safety_2_state = _test_state()
_test_away_safety_2_result = away_safety_2(_test_away_safety_2_state)
assert_equal(type(_test_away_safety_2_result).__name__, "Page")
assert_equal(_test_away_safety_2_state.away_score, 12)

_test_home_safety_2_state = _test_state()
_test_home_safety_2_result = home_safety_2(_test_home_safety_2_state)
assert_equal(type(_test_home_safety_2_result).__name__, "Page")
assert_equal(_test_home_safety_2_state.home_score, 12)

_test_away_safety_OT_state = _test_state()
_test_away_safety_OT_result = away_safety_OT(_test_away_safety_OT_state)
assert_equal(type(_test_away_safety_OT_result).__name__, "Page")
assert_equal(_test_away_safety_OT_state.away_score, 12)

_test_home_safety_OT_state = _test_state()
_test_home_safety_OT_result = home_safety_OT(_test_home_safety_OT_state)
assert_equal(type(_test_home_safety_OT_result).__name__, "Page")
assert_equal(_test_home_safety_OT_state.home_score, 12)

_test_away_one_point_state = _test_state()
_test_away_one_point_result = away_one_point(_test_away_one_point_state)
assert_equal(type(_test_away_one_point_result).__name__, "Page")
assert_equal(_test_away_one_point_state.away_score, 11)
assert_equal(_test_away_one_point_state.away_conversion_att, 3)
assert_equal(_test_away_one_point_state.away_conversion_made, 2)

_test_home_one_point_state = _test_state()
_test_home_one_point_result = home_one_point(_test_home_one_point_state)
assert_equal(type(_test_home_one_point_result).__name__, "Page")
assert_equal(_test_home_one_point_state.home_score, 11)
assert_equal(_test_home_one_point_state.home_conversion_att, 3)
assert_equal(_test_home_one_point_state.home_conversion_made, 2)

_test_away_one_point_2_state = _test_state()
_test_away_one_point_2_result = away_one_point_2(_test_away_one_point_2_state)
assert_equal(type(_test_away_one_point_2_result).__name__, "Page")
assert_equal(_test_away_one_point_2_state.away_score, 11)
assert_equal(_test_away_one_point_2_state.away_conversion_att, 3)
assert_equal(_test_away_one_point_2_state.away_conversion_made, 2)

_test_home_one_point_2_state = _test_state()
_test_home_one_point_2_result = home_one_point_2(_test_home_one_point_2_state)
assert_equal(type(_test_home_one_point_2_result).__name__, "Page")
assert_equal(_test_home_one_point_2_state.home_score, 11)
assert_equal(_test_home_one_point_2_state.home_conversion_att, 3)
assert_equal(_test_home_one_point_2_state.home_conversion_made, 2)

_test_away_one_point_OT_state = _test_state()
_test_away_one_point_OT_result = away_one_point_OT(_test_away_one_point_OT_state)
assert_equal(type(_test_away_one_point_OT_result).__name__, "Page")
assert_equal(_test_away_one_point_OT_state.away_score, 11)
assert_equal(_test_away_one_point_OT_state.away_conversion_att, 3)
assert_equal(_test_away_one_point_OT_state.away_conversion_made, 2)

_test_home_one_point_OT_state = _test_state()
_test_home_one_point_OT_result = home_one_point_OT(_test_home_one_point_OT_state)
assert_equal(type(_test_home_one_point_OT_result).__name__, "Page")
assert_equal(_test_home_one_point_OT_state.home_score, 11)
assert_equal(_test_home_one_point_OT_state.home_conversion_att, 3)
assert_equal(_test_home_one_point_OT_state.home_conversion_made, 2)

_test_away_punt_state = _test_state()
_test_away_punt_result = away_punt(_test_away_punt_state)
assert_equal(type(_test_away_punt_result).__name__, "Page")
assert_equal(_test_away_punt_state.away_punt, 3)

_test_home_punt_state = _test_state()
_test_home_punt_result = home_punt(_test_home_punt_state)
assert_equal(type(_test_home_punt_result).__name__, "Page")
assert_equal(_test_home_punt_state.home_punt, 3)

_test_away_punt_2_state = _test_state()
_test_away_punt_2_result = away_punt_2(_test_away_punt_2_state)
assert_equal(type(_test_away_punt_2_result).__name__, "Page")
assert_equal(_test_away_punt_2_state.away_punt, 3)

_test_home_punt_2_state = _test_state()
_test_home_punt_2_result = home_punt_2(_test_home_punt_2_state)
assert_equal(type(_test_home_punt_2_result).__name__, "Page")
assert_equal(_test_home_punt_2_state.home_punt, 3)

_test_away_punt_OT_state = _test_state()
_test_away_punt_OT_result = away_punt_OT(_test_away_punt_OT_state)
assert_equal(type(_test_away_punt_OT_result).__name__, "Page")
assert_equal(_test_away_punt_OT_state.away_punt, 3)

_test_home_punt_OT_state = _test_state()
_test_home_punt_OT_result = home_punt_OT(_test_home_punt_OT_state)
assert_equal(type(_test_home_punt_OT_result).__name__, "Page")
assert_equal(_test_home_punt_OT_state.home_punt, 3)

_test_away_turnover_state = _test_state()
_test_away_turnover_result = away_turnover(_test_away_turnover_state)
assert_equal(type(_test_away_turnover_result).__name__, "Page")
assert_equal(_test_away_turnover_state.away_turnover, 3)

_test_home_turnover_state = _test_state()
_test_home_turnover_result = home_turnover(_test_home_turnover_state)
assert_equal(type(_test_home_turnover_result).__name__, "Page")
assert_equal(_test_home_turnover_state.home_turnover, 3)

_test_away_turnover_2_state = _test_state()
_test_away_turnover_2_result = away_turnover_2(_test_away_turnover_2_state)
assert_equal(type(_test_away_turnover_2_result).__name__, "Page")
assert_equal(_test_away_turnover_2_state.away_turnover, 3)

_test_home_turnover_2_state = _test_state()
_test_home_turnover_2_result = home_turnover_2(_test_home_turnover_2_state)
assert_equal(type(_test_home_turnover_2_result).__name__, "Page")
assert_equal(_test_home_turnover_2_state.home_turnover, 3)

_test_away_turnover_OT_state = _test_state()
_test_away_turnover_OT_result = away_turnover_OT(_test_away_turnover_OT_state)
assert_equal(type(_test_away_turnover_OT_result).__name__, "Page")
assert_equal(_test_away_turnover_OT_state.away_turnover, 3)

_test_home_turnover_OT_state = _test_state()
_test_home_turnover_OT_result = home_turnover_OT(_test_home_turnover_OT_state)
assert_equal(type(_test_home_turnover_OT_result).__name__, "Page")
assert_equal(_test_home_turnover_OT_state.home_turnover, 3)

_test_away_turnover_on_downs_state = _test_state()
_test_away_turnover_on_downs_result = away_turnover_on_downs(_test_away_turnover_on_downs_state)
assert_equal(type(_test_away_turnover_on_downs_result).__name__, "Page")

_test_home_turnover_on_downs_state = _test_state()
_test_home_turnover_on_downs_result = home_turnover_on_downs(_test_home_turnover_on_downs_state)
assert_equal(type(_test_home_turnover_on_downs_result).__name__, "Page")

_test_away_turnover_on_downs_2_state = _test_state()
_test_away_turnover_on_downs_2_result = away_turnover_on_downs_2(_test_away_turnover_on_downs_2_state)
assert_equal(type(_test_away_turnover_on_downs_2_result).__name__, "Page")

_test_home_turnover_on_downs_2_state = _test_state()
_test_home_turnover_on_downs_2_result = home_turnover_on_downs_2(_test_home_turnover_on_downs_2_state)
assert_equal(type(_test_home_turnover_on_downs_2_result).__name__, "Page")

_test_away_turnover_on_downs_OT_state = _test_state()
_test_away_turnover_on_downs_OT_result = away_turnover_on_downs_OT(_test_away_turnover_on_downs_OT_state)
assert_equal(type(_test_away_turnover_on_downs_OT_result).__name__, "Page")

_test_home_turnover_on_downs_OT_state = _test_state()
_test_home_turnover_on_downs_OT_result = home_turnover_on_downs_OT(_test_home_turnover_on_downs_OT_state)
assert_equal(type(_test_home_turnover_on_downs_OT_result).__name__, "Page")

_test_halftime_state = _test_state()
_test_halftime_result = halftime(_test_halftime_state)
assert_equal(type(_test_halftime_result).__name__, "Page")

_test_second_half_ball_state = _test_state()
_test_second_half_ball_result = second_half_ball(_test_second_half_ball_state)
assert_equal(type(_test_second_half_ball_result).__name__, "Page")

_test_overtime_cointoss_state = _test_state()
_test_overtime_cointoss_result = overtime_cointoss(_test_overtime_cointoss_state)
assert_equal(type(_test_overtime_cointoss_result).__name__, "Page")

_test_away_overtime_state = _test_state()
_test_away_overtime_result = away_overtime(_test_away_overtime_state)
assert_equal(type(_test_away_overtime_result).__name__, "Page")

_test_home_overtime_state = _test_state()
_test_home_overtime_result = home_overtime(_test_home_overtime_state)
assert_equal(type(_test_home_overtime_result).__name__, "Page")

_test_final_state = _test_state()
_test_final_result = final(_test_final_state)
assert_equal(type(_test_final_result).__name__, "Page")


start_server(State(Team("",""),Team("",""),0,0,0,0,0,0,0,0,0,0,0,0,0,0,Team("","")))
