#database 

def nba_data():

    lakers= """
                    Luka Doncic:(28.2 ppg, 7.5 apg, 8.1 rpg, 0.438* fg) 
                    Lebron James:(24.4 ppg, 8.2 apg, 7.8 rpg, 0.513* fg)
                    Austin Reeves:(20.2 ppg, 5.8 apg, 4.5 rpg, 0.460* fg)
                    Rui Hachimura:(13.1 ppg, 1.4 apg, 5.0 rpg, 0.509* fg)
                    Jackson Hayes:(6.8 ppg, 1.0 apg, 4.8 rpg, 0.722* fg) 
                    """
    sixers= """
                    Tyrese Maxey:(26.3 ppg, 6.1 apg, 3.3 rpg, 0.437* fg)
                    Paul George:(16.2 ppg, 4.3 apg, 5.3 rpg, 0.430* fg)
                    Kelly Oubre:(15.1 ppg, 1.8 apg, 6.1 rpg, 0.469* fg)
                    Quentin Grimes:(21.9 ppg, 4.5 apg, 5.2 rpg, 0.469* fg)
                    Joel Embid:(23.8 ppg, 4.5 apg, 8.2 rpg, 0.444* fg) 
                    """

    bucks= """
                    Damian Lillard:(24.9 ppg, 7.1 apg, 4.7 rpg, 0.448* fg)
                    Giannis Antetokounmpo:(30.4 ppg, 6.5 apg, 11.9 rpg, 0.601* fg)
                    Kyle Kuzma:(14.5 ppg, 2.2 apg, 5.6 rpg, 0.455* fg)
                    Brook Lopez:(13.0 ppg, 1.8 apg, 5.0 rpg, 0.509* fg)
                    Taurean Prince:(8.2 ppg, 1.9 apg, 3.6 rpg, 0.457* fg) 
                    """

    suns= """
                    Devin Booker:(25.6 ppg, 7.1 apg, 4.1 rpg, 0.461* fg)
                    Kevin Durant:(26.6 ppg, 4.2 apg, 6.0 rpg, 0.527* fg)
                    Bradley Beal:(17.0 ppg, 3.7 apg, 3.3 rpg, 0.497* fg)
                    Royce O' Neal:(9.1 ppg, 2.2 apg, 4.7 rpg, 0.423* fg)
                    Jusuf Nurkic:(8.6 ppg, 1.9 apg, 9.2 rpg, 0.454* fg)
                    """

    jazz= """
                    Keyonte George:(16.8 ppg, 5.6 apg, 3.8 rpg, 0.391* fg)
                    Lauri Markkanen:(19.0 ppg, 1.5 apg, 5.9 rpg, 0.423* fg)
                    John Collins:(19.0 ppg, 2.0 apg, 8.2 rpg, 0.527* fg)
                    Colin Sexton:(18.4 ppg, 4.2 apg, 2.7 rpg, 0.480* fg)
                    Walker Kessler:(11.1 ppg, 1.7 apg, 12.2 rpg, 0.663* fg)
                    """

    mavericks= """
                        Kyrie Irving:(24.7 ppg, 4.6 apg, 4.8 rpg, 0.473* fg)
                        Anthony Davis:(20.0 ppg, 4.4 apg, 10.1 rpg, 0.461* fg)
                        PJ Washington:(14.7 ppg, 2.3 apg, 7.8 rpg, 0.453* fg)
                        Klay Thompson:(14.0 ppg, 2.0 apg, 3.4 rpg, 0.412* fg)
                        Daniel Gafford:(12.3 ppg, 1.4 apg, 6.8 rpg, 0.702* fg)
                        """

    nets= """
                    Cameron Johnson:(18.8 ppg, 3.4 apg, 4.3 rpg, 0.475* fg)
                    Cam Thomas:(24.0 ppg, 3.8 apg, 3.3 rpg, 0.438* fg)
                    Nic claxton:(10.3 ppg, 2.2 apg, 7.4 rpg, 0.563* fg)
                    D'Angelo Russel:(12.9 ppg, 5.6 apg, 2.8 rpg, 0.367* fg)
                    Dennis Schroder:(18.4 ppg, 6.6 apg, 3.0 rpg, 0.452* fg)
                    """

    warriors= """
                        Steph Curry:(24.5 ppg, 6.0 apg, 4.4 rpg, 0.448* fg)
                        Jimmy Butler:(17.9 ppg, 5.9 apg, 5.5 rpg, 0.476* fg)
                        Draymond Green:(9.0 ppg, 5.6 apg, 6.1 rpg, 0.424* fg)
                        Buddy Hield:(11.1 ppg, 1.6 apg, 3.2 rpg, 0.417* fg)
                        Brandin Podzmiemski:(11.7 ppg, 3.4 apg, 5.1 rpg, 0.445* fg)
                        """

    thunder= """
                        Shai Gilgeous Alexander:(32.7 ppg, 6.4 apg, 5.0 rpg, 0.519* fg)
                        Jalen Williams:(21.6 ppg, 5.1 apg, 5.3 rpg, 0.484* fg)
                        Luguentz Dort:(10.1 ppg, 1.6 apg, 4.1 rpg, 0.435 fg)
                        Chet Holmgren:(15.0 ppg, 2.0 apg, 8.0 rpg, 0.490* fg)
                        Isiah Hartenstein:( 11.2 ppg, 3.8 apg, 10.7 rpg, 0.581* fg) 
                        """

    knicks= """
                    Jalen Brunson:(26.0 ppg, 7.3 apg, 2.9 rpg, 0.488* fg)
                    OG Anunoby:(18.0 ppg, 2.2 apg, 4.8 rpg, 0.476* fg)
                    Karl Anthony Towns:(24.4 ppg, 3.1 apg, 12.8 rpg, 0.526* fg)
                    Mikal Bridges:(17.6 ppg, 3.7 apg, 3.2 rpg, 0.500* fg)
                    Josh Hart:(13.6 ppg, 5.9 apg, 9.6 rpg, 0.525* fg)
                    """

    celtics= """
                        Jason Tatum:(26.8 ppg, 6.0 apg, 8.7 rpg, 0.452* fg)
                        Jaylen Brown:(22.2 ppg, 4.5 apg, 5.8 rpg, 0.463* fg)
                        Kristaps Porzingis:(19.5 ppg, 2.1 apg, 6.8 rpg, 0.483* fg)
                        Derrick White:(16.4 ppg, 4.8 apg, 4.5 rpg, 0.442* fg)
                        Al Horford:(9.0 ppg, 2.1 apg, 6.2 rpg, 0.423* fg)
                        """

    nuggets= """
                        Nikola Jokic:(29.6 ppg, 10.2 apg, 12.7 rpg, 0.576* fg)
                        Jamal Murray:(21.4 ppg, 6.0 apg, 3.9 rpg, 0.474* fg)
                        Michael Porter Jr:(18.2 ppg, 2.1 apg, 7.0 rpg, 0.504* fg)
                        Aaron Gordon:(14.7 ppg, 3.2 apg, 4.8 rpg, 0.531* fg)
                        Christian Braun:(15.4 ppg, 2.6 apg, 5.2 rpg, 0.580* fg) 
                        """

    pacers= """
                    Tyrese Haliburton:(18.6 ppg, 9.2 apg, 3.5 rpg, 0.473* fg)
                    Pascal Siakam:(20.2 ppg, 3.4 apg, 6.9 rpg, 0.519* fg)
                    Myles Turner:(15.6 ppg, 1.5 apg, 6.5 rpg, 0.481* fg)
                    Obi Toppin:(10.5 ppg, 1.6 apg, 4.0 rpg, 0.529* fg)
                    Aaron Nesmith:(12.0 ppg, 1.2 apg, 4.0 rpg, 0.507* fg) 
                    """

    rockets= """
                        Amen Thompson:(14.1 ppg, 3.8 apg, 8.2 rpg, 0.557* fg)
                        Dillon Brooks:(14.0 ppg, 1.7 apg, 3.7 rpg, 0.429* fg)
                        Alperen Sengun:(19.1 ppg, 4.9 apg, 10.3 rpg, 0.496* fg)
                        Fred Vanvleet:(14.1 ppg, 5.6 apg, 3.7 rpg, 0.378* fg)
                        Jalen Green:(21.0 ppg, 3.4 apg, 4.6 rpg, 0.423* fg)
                    """

    heat= """
                    Andrew Wiggins:(19.0 ppg, 3.3 apg, 4.2 rpg, 0.458* fg)
                    Bam Adebayo:(18.1 ppg, 4.3 apg, 9.6 rpg, 0.485* fg)
                    Tyler Herro:(23.9 ppg, 5.5 apg, 5.2 rpg, 0.472* fg)
                    Davion Mitchell:(10.3 ppg, 5.3 apg, 2.7 rpg, 0.504* fg)
                    Terry Rozier:(10.6 ppg, 2.6 apg, 3.7 rpg, 0.391* fg) 
                    """

    spurs= """
                    Victor Wembyenama:(24.3 ppg, 3.7 apg, 11.0 rpg, 0.476* fg)
                    Stephon Castle:(14.7 ppg, 4.1 apg, 3.7 rpg, 0.428* fg)
                    Jeremy Sochan:(11.4 ppg, 2.4 apg, 6.5 rpg, 0.535* fg)
                    Chris Paul:(8.8 ppg, 7.4 apg, 3.6 rpg, 0.427* fg)
                    De'aaron Fox:(19.7 ppg, 6.8 apg, 4.3 rpg, 0.446* fg) 
                    """

    cavaliers= """
                        Darius Garland:(20.6 ppg, 6.7 apg, 2.9 rpg, 0.472* fg)
                        Donovon Mitchell:(24.0 ppg, 5.0 apg, 4.5 rpg, 0.443* fg)
                        Jarret Allen:(13.5 ppg, 1.9 apg, 9.7 rpg, 0.706* fg)
                        Evan Mobely:(18.5 ppg, 3.2 apg, 9.3 rpg, 0.557* fg)
                        Ty Jerome:(12.5 ppg, 3.4 apg, 2.5 rpg, 0.516* fg)
                        """

    bulls= """
                    Coby White:(20.4 ppg, 4.5 apg, 3.7 rpg, 0.453* fg)
                    Nikola Vucevic:(18.5 ppg, 3.4 apg, 11.0 rpg, 0.516* fg)
                    Josh Giddey:(14.6 ppg, 6.2 apg, 7.4 rpg, 0.456* fg)
                    Patrick Williams:(11.5 ppg, 1.8 apg, 4.2 rpg, 0.465* fg)
                    Matas Buzelis:(8.6 ppg, 2.1 apg, 3.4 rpg, 0.432* fg) 
                    """
    clippers= """
                        Kawhi Leonard:(21.5 ppg, 4.8 apg, 6.2 rpg, 0.498* fg)
                        Ivaca Zubac;(16.8 ppg, 1.8 apg, 12.6 rpg, 0.642* fg)
                        Norman Powell:(21.8 ppg, 2.4 apg, 3.0 rpg, 0.484* fg)
                        James Harden:(22.8 ppg, 8.7 apg, 5.4 rpg, 0.410* fg)
                        Derrick Jones Jr:(10.1 ppg, 1.2 apg, 3.5 rpg, 0.526* fg) 
                        """

    raptors= """
                        Scottie Barnes:(19.3 ppg, 5.8 apg, 7.6 rpg, 0.446* fg)
                        RJ Barret:(21.1 ppg, 5.4 apg, 6.3 rpg, 0.468* fg)
                        Jakob Poeltl:(14.5 ppg, 2.1 apg, 9.8 rpg, 0.627* fg)
                        Gradey Dick:(14.4 ppg, 1.8 ppg, 3.6 rpg, 0.410* fg)
                        Immanuel Quickley:(17.1 ppg, 5.8 apg, 3.5 rpg, 0.420* fg) 
                        """
    pistons= """
                        Cade Cunningham:(26.1 ppg, 9.1 apg, 6.1 rpg, 0.469* fg)
                        Malik Beasley:(16.3 ppg, 1.7 apg, 2.6 rpg, 0.430* fg)
                        Jalen Duren:(11.8 ppg, 2.7 apg, 10.3 rpg, 0.692* fg)
                        Jaden Ivey:(17.6 ppg, 4.0 apg, 4.1 rpg, 0.460* fg)
                        Tobias Harris:(13.7 ppg, 2.2 apg, 5.9 rpg, 0.469* fg) 
                        """

    kings= """
                    Zach Lavine:(22.4 ppg, 3.8 apg, 3.5 rpg, 0.511* fg)
                    Malik Monk:(17.2 ppg, 5.6 apg, 3.8 rpg, 0.439* fg)
                    DeMar DeDerozan:(22.2 ppg, 4.4 apg, 3.9 rpg, 0.477* fg)
                    Keegan Murray:(12.4 ppg, 1.4 apg, 6.7 rpg, 0.444* fg)
                    Domantas Sabonis:(19.1 ppg, 6.0 apg, 13.9 rpg, 0.590* fg) 
                    """

    timberwolves= """
            Anthony Edwards:(27.6 ppg, 4.5 apg, 5.7 rpg, 0.447* fg)
            Jaden Mcdaniels:(12.2 ppg, 2.0 apg, 5.7 rpg, 0.477* fg)
            Naz Ried:(14.2 ppg, 1.5 apg, 6.0 rpg, 0.462* fg)
            Julius Randle:(18.7 ppg, 4.7 apg, 7.1 rpg, 0.485* fg)
            Mike Conley:(8.2 ppg, 4.5 apg, 2.4 rpg, 0.407* fg) 
            """

    trailblazers= """
                        Anfrenee Simons:(19.3 ppg, 4.1 apg, 2.6 rpg, 0.426* fg)
                        Deandre Ayton:(14.4 ppg, 1.8 apg, 10.0 rpg, 0.566* fg)
                        Shaedon Sharpe:(18.5 ppg, 3.2 apg, 4.0 rpg, 0.451* fg)
                        Deni Avdija:(16.9 ppg, 2.9 apg, 7.3 rpg, 0.476* fg)
                        Scoot Henderson:(12.7 ppg, 5.0 apg, 3.9 rpg, 0.419* fg) 
                        """

    hawks= """
                    Trae Young:(24.2 ppg, 11.6 apg, 3.0 rpg, 0.411* fg)
                    Dyson Daniels:(14.1 ppg, 5.0 apg, 4.2 rpg, 0.493* fg)
                    Georges Niang:(12.1 ppg, 1.8 apg, 4.0 rpg, 0.441* fg)
                    Clint Capela:(8.9 ppg, 1.0 apg, 10.2 rpg, 0.559* fg)
                    Zaccharie Risacher:(12.6 ppg, 2.1 apg, 3.8 rpg, 0.458* fg) 
                    """

    grizzlies= """
                        Ja Morant:(23.2 ppg, 7.9 apg, 4.1 rpg, 0.451* fg)
                        Desmond Bane:(19.2 ppg, 5.3 apg, 6.1 rpg, 0.484* fg)
                        Jaren Jackson Jr:(22.2 ppg, 1.9 apg, 5.6 rpg, 0.488* fg)
                        Zach Edey:(9.2 ppg, 1.2 apg, 7.8 rpg, 0.580* fg)
                        Scottie Pippen Jr:(9.9 ppg, 4.4 apg, 3.3 rpg, 0.480* fg) 
                        """

    pelicans= """
                        Zion Williamson:(24.6 ppg, 4.9 apg, 6.8 rpg, 0.567* fg)
                        Brandon Ingram:(22.2 ppg, 5.1 apg, 5.6 rpg, 0.468* fg)
                        CJ McCollum:(21.1 ppg, 4.1 apg, 4.2 rpg, 0.440* fg)
                        Jonas Valanciunas:(11.5 ppg, 1.5 apg, 9.8 rpg, 0.540* fg)
                        Herb Jones:(10.3 ppg, 3.3 apg, 4.5 rpg, 0.436* fg) 
                        """

    hornets= """
                        LaMelo Ball:(25.2 ppg, 7.4 apg, 4.9 rpg, 0.405* fg)
                        Miles Bridges:(20.3 ppg, 3.2 apg, 6.8 rpg, 0.431* fg)
                        Brandon Miller:(21.0 ppg, 2.8 apg, 4.5 rpg, 0.403* fg)
                        Mark Williams:(15.3 ppg, 1.8 apg, 10.2 rpg, 0.604* fg)
                        Grant Williams:(10.4 ppg, 1.5 apg, 4.2 rpg, 0.444* fg) 
                        """

    wizards= """
                        Jordan Poole:(20.5 ppg, 4.2 apg, 3.1 rpg, 0.432* fg)
                        Corey Kispert:(11.6 ppg, 2.0 apg, 3.4 rpg, 0.456* fg)
                        Alexander Sarr:(13.0 ppg, 2.1 apg, 4.0 rpg, 0.394* fg)
                        Khris Middleton:(10.7 ppg, 2.3 apg, 4.1 rpg, 0.413* fg)
                        Bub Carrington:(9.8 ppg, 1.5 apg, 3.2 rpg, 0.401* fg) 
                        """

    magic= """
                    Paulo Banchero:(25.9 ppg, 4.8 apg, 7.9 rpg, 0.452* fg)
                    Franz Wagner:(24.2 ppg, 4.1 apg, 5.6 rpg, 0.468* fg)
                    Wendell Carter Jr:(9.1 ppg, 1.5 apg, 7.0 rpg, 0.460* fg)
                    Cole Anthony:(9.4 ppg, 3.2 apg, 3.5 rpg, 0.424* fg)
                    Jalen Suggs:(16.2 ppg, 4.0 apg, 3.8 rpg, 0.410* fg) 
                    """


    allstars= """
        Tyler Herro, Cade Cunningham, Evan Mobely, Darius Garland, Jalen Williams,
        Jaren Jackson Jr, Jaleen Brunson, Anothony Edwards, Trae Young, Donovan Mitchell, 
        Karl Anthony Towns, Alperen Sengun, Pascal Siakam, Victor Wembyenama, 
        Shai Gigeous Alexander, Giannis Antetokoumpo, Nikola Jokic, Kyrie Irving, Jaylen Brown, 
        James Harden, Damian Lillard, Kevin Durant, Jayson Tatum, Anthony Davis, Steph Curry, 
        Lebron James 
        """


    teams = {
        "lakers": lakers,
        "sixers": sixers,
        "bucks": bucks,
        "suns": suns,
        "jazz": jazz,
        "mavericks": mavericks,
        "nets": nets,
        "warriors": warriors,
        "thunder": thunder,
        "knicks": knicks,
        "celtics": celtics,
        "nuggets": nuggets,
        "pacers": pacers,
        "rockets": rockets,
        "heat": heat,
        "spurs": spurs,
        "cavaliers": cavaliers,
        "bulls": bulls,
        "clippers": clippers,
        "raptors": raptors,
        "pistons": pistons,
        "kings": kings,
        "timberwolves": timberwolves,
        "trailblazers": trailblazers,
        "hawks": hawks,
        "grizzlies": grizzlies,
        "pelicans": pelicans,
        "hornets": hornets,
        "wizards": wizards,
        "magic": magic
    }
