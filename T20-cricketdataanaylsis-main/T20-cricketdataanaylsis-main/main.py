from imaplib import _Authenticator
import random
import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
import database as db
import matplotlib.pyplot as plt
import plotly.express as px
import csv
import xlsxwriter
import io

# user authentication
users = db.fecth_all_users()
usernames = [user["key"] for user in users]
names = [user["name"] for user in users]
hashed_password = [user["password"] for user in users]


authenticator = stauth.Authenticate(names, usernames, hashed_password, "Home", "abcdef", cookie_expiry_days=1 )

name, authentication_status, username = authenticator.login("Login", "main")


if authentication_status:
   authenticator.logout('Logout', 'main')
   if st.session_state["authentication_status"]:
    
    # Add a sidebar
    # st.sidebar.title("Navigation")
    st.title("T20 Criketer Data Analysis App")
    st.write(f'Welcomes *{st.session_state["name"]}*')
    rad = option_menu(
            menu_title="Navigation",
            options=["Home","Openers", "Middle Order", "Lower-Middle Order", "Finishers", "Bowlers", "Make your team"],
            icons=["none","none","none","none","none","none", "none"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
    # with st.sidebar:
        
            styles={
                "container":{"padding": "0!important", "backgroubd-color":"red"},
                "icon": {"color":"orange", "font-size": "16px"},
                "nav-link":{
                "font-size": "16px",
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "#eee",
                },
            "nav-link-selected":{"background-color": "green"},
            },
        )
        
    # Title of the app
    if rad =="Home":
            st.header("Introduction")
            st.write("Cricket analytics provides interesting insights into the game and predictive intelligence regarding game outcomes. Overall, this project aims to demonstrate the importance of data analysis in cricket and how it can be used to improve player and team performance. Through this analysis, we hope to provide insights that can be used by coaches, selectors, and fans to make informed decisions about their favorite players and teams.")
            st.image("img.png")
            
                    

    if rad =="Openers":
        # To display table
                    data = pd.read_csv("openers.csv")
                    st.sidebar.header("Please Filter Here: ")
                    p_t = st.sidebar.multiselect("Select the Team: ",
                                    options=data["team"].unique(), 
                                    default=[data["team"].iloc[0]])

                    p_bp = st.sidebar.multiselect("Select the Batting Position: ",
                                    options=data["BattingPosition"].unique(), 
                                    #   default=[random.choice(data["BattingPosition"].unique())])
                                    default=[data["BattingPosition"].unique()[10]])

                    p_br = st.sidebar.multiselect("Select the Total Innings Batted: ", 
                                    options=data["Total_Innings_Batted"].unique(), 
                                    default=[data["Total_Innings_Batted"].unique()[5]])
                    df_selection = data.query(
                                  "team == @p_t & BattingPosition == @p_bp & Total_Innings_Batted == @p_br"
                     )  
                    
                    st.dataframe(df_selection) 

                    
                    rad1 = option_menu(
                            menu_title="Graphical Representation",
                            options=["Total Runs","Batting Average", "Strike Rate", "Boundary %"],
                            icons=["none","none","none","none","none"],
                            menu_icon="cast",
                            default_index=0,
                            orientation="horizontal",
                    # with st.sidebar:
        
                            styles={
                                "container":{"padding": "0!important", "backgroubd-color":"red"},
                                "icon": {"color":"orange", "font-size": "10px"},
                                "nav-link":{
                                "font-size": "10px",
                                "text-align": "center",
                                "margin": "0px",
                                "--hover-color": "#eee",
                                },
                            "nav-link-selected":{"background-color": "green"},
                            },
                        )     
                    if rad1 == "Total Runs":         
                        if len(df_selection) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p0 = px.bar(
                                x=df_selection["Total_Runs"],  
                                y=df_selection["name"],
                                orientation="h",
                                title="<b>Runs by players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection["Total_Runs"]),
                                template="plotly_white"
                            )


                            runs_p_p0.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p0)
                            
                            
                            
                        if len(df_selection) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection["Total_Runs"],  
                                y=df_selection["name"],
                                orientation="h",
                                title="<b>Runs by players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection["Total_Runs"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection["Total_Runs"],  
                                y=df_selection["name"],
                                # orientation="h",
                                title="<b>Runs by players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)
                            
                  
                            
                    if rad1 == "Batting Average":         
                        if len(df_selection) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p = px.bar(
                                x=df_selection["Batting_Avg"],  
                                y=df_selection["name"],
                                orientation="h",
                                title="<b>Batting Average of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection["Batting_Avg"]),
                                template="plotly_white"
                            )


                            runs_p_p.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p)
                            
                        if len(df_selection) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection["Batting_Avg"],  
                                y=df_selection["name"],
                                orientation="h",
                                title="<b>Batting Average of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection["Batting_Avg"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection["Batting_Avg"],  
                                y=df_selection["name"],
                                # orientation="h",
                                title="<b>Batting Average of players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)
                            
                    if rad1 == "Strike Rate":         
                        if len(df_selection) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p = px.bar(
                                x=df_selection["Strike_rate"],  
                                y=df_selection["name"],
                                orientation="h",
                                title="<b>Strike Rate of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection["Strike_rate"]),
                                template="plotly_white"
                            )


                            runs_p_p.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p)
                            
                        if len(df_selection) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection["Strike_rate"],  
                                y=df_selection["name"],
                                orientation="h",
                                title="<b>Strike Rate of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection["Strike_rate"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection["Strike_rate"],  
                                y=df_selection["name"],
                                # orientation="h",
                                title="<b>Strike Rate of players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)
                            
                    if rad1 == "Boundary %":         
                        if len(df_selection) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p = px.bar(
                                x=df_selection["Boundary%"],  
                                y=df_selection["name"],
                                orientation="h",
                                title="<b>Boundary% of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection["Boundary%"]),
                                template="plotly_white"
                            )


                            runs_p_p.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p)
                            
                        if len(df_selection) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection["Boundary%"],  
                                y=df_selection["name"],
                                orientation="h",
                                title="<b>Boundary% of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection["Boundary%"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection["Boundary%"],  
                                y=df_selection["name"],
                                # orientation="h",
                                title="<b>Boundary% of players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)
    
    if rad =="Middle Order":
            # To display table
                data1 = pd.read_csv("MiddleOrder.csv")
                # st.dataframe(data1)
                st.sidebar.header("Please Filter Here: ")
                p_t1= st.sidebar.multiselect("Select the Team: ",
                                    options=data1["team"].unique(), 
                                    default=[data1["team"].iloc[2]])
                 
                p_bp1 = st.sidebar.multiselect("Select the Batting Position: ",
                                    options=data1["Batting_Position"].unique(), 
                                    default=[data1["Batting_Position"].unique()[3]])

                p_br1 = st.sidebar.multiselect("Select the Total Innings Batted: ", 
                                    options=data1["Total_Innings_Batted"].unique(), 
                                    default=[data1["Total_Innings_Batted"].unique()[7]])
                
                df_selection1 = data1.query(
                                  "team == @p_t1 & Batting_Position == @p_bp1 & Total_Innings_Batted == @p_br1"
                    )   
                st.dataframe(df_selection1)
                
                
                rad1 = option_menu(
                            menu_title="Graphical Representation",
                            options=["Total Runs","Batting Average", "Strike Rate", "Boundary %"],
                            icons=["none","none","none","none","none"],
                            menu_icon="cast",
                            default_index=0,
                            orientation="horizontal",
                    # with st.sidebar:
        
                            styles={
                                "container":{"padding": "0!important", "backgroubd-color":"red"},
                                "icon": {"color":"orange", "font-size": "10px"},
                                "nav-link":{
                                "font-size": "10px",
                                "text-align": "center",
                                "margin": "0px",
                                "--hover-color": "#eee",
                                },
                            "nav-link-selected":{"background-color": "green"},
                            },
                        )     
                if rad1 == "Total Runs":         
                        if len(df_selection1) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p0 = px.bar(
                                x=df_selection1["Total_Runs"],  
                                y=df_selection1["name"],
                                orientation="h",
                                title="<b>Runs by players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection1["Total_Runs"]),
                                template="plotly_white"
                            )


                            runs_p_p0.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p0)
                            
                        if len(df_selection1) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection1["Total_Runs"],  
                                y=df_selection1["name"],
                                orientation="h",
                                title="<b>Runs by players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection1["Total_Runs"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection1) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection1["Total_Runs"],  
                                y=df_selection1["name"],
                                # orientation="h",
                                title="<b>Runs by players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)
                            
                if rad1 == "Batting Average":         
                        if len(df_selection1) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p = px.bar(
                                x=df_selection1["Batting_Avg"],  
                                y=df_selection1["name"],
                                orientation="h",
                                title="<b>Batting Average of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection1["Batting_Avg"]),
                                template="plotly_white"
                            )


                            runs_p_p.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p)
                            
                        if len(df_selection1) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection1["Batting_Avg"],  
                                y=df_selection1["name"],
                                orientation="h",
                                title="<b>Batting Average of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection1["Batting_Avg"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection1) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection1["Batting_Avg"],  
                                y=df_selection1["name"],
                                # orientation="h",
                                title="<b>Batting Average of players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)
                            
                if rad1 == "Strike Rate":         
                        if len(df_selection1) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p = px.bar(
                                x=df_selection1["Strike_rate"],  
                                y=df_selection1["name"],
                                orientation="h",
                                title="<b>Strike Rate of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection1["Strike_rate"]),
                                template="plotly_white"
                            )


                            runs_p_p.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p)
                            
                        if len(df_selection1) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection1["Strike_rate"],  
                                y=df_selection1["name"],
                                orientation="h",
                                title="<b>Strike Rate of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection1["Strike_rate"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection1) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection1["Strike_rate"],  
                                y=df_selection1["name"],
                                # orientation="h",
                                title="<b>Strike Rate of players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)
                            
                if rad1 == "Boundary %":         
                        if len(df_selection1) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p = px.bar(
                                x=df_selection1["Boundary%"],  
                                y=df_selection1["name"],
                                orientation="h",
                                title="<b>Boundary % of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection1["Boundary%"]),
                                template="plotly_white"
                            )


                            runs_p_p.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p)
                            
                        if len(df_selection1) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection1["Boundary%"],  
                                y=df_selection1["name"],
                                orientation="h",
                                title="<b>Boundary % of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection1["Boundary%"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection1) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection1["Boundary%"],  
                                y=df_selection1["name"],
                                # orientation="h",
                                title="<b>Boundary % of players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)
        
    if rad =="Lower-Middle Order":
            # To display table
                data2 = pd.read_csv("LowerMiddleOrder.csv")
                st.sidebar.header("Please Filter Here: ")
                p_t2= st.sidebar.multiselect("Select the Team: ",
                                    options=data2["team"].unique(), 
                                    default=[data2["team"].iloc[19]])
                 
                p_bp2 = st.sidebar.multiselect("Select the Batting Position: ",
                                    options=data2["Batting_Position"].unique(), 
                                    default=[data2["Batting_Position"].unique()[3]])

                p_br2 = st.sidebar.multiselect("Select the Total Innings Batted: ", 
                                    options=data2["Total_Innings_Batted"].unique(), 
                                    default=[data2["Total_Innings_Batted"].unique()[2]])
                
                df_selection2 = data2.query(
                                  "team == @p_t2 & Batting_Position == @p_bp2 & Total_Innings_Batted == @p_br2"
                    )   
                st.dataframe(df_selection2)
                
                
                rad1 = option_menu(
                            menu_title="Graphical Representation",
                            options=["Total Runs","Batting Average", "Strike Rate","Wickets", "Bowling Strike Rate", "Economy"],
                            icons=["none","none","none","none","none", "none", "none", "none"],
                            menu_icon="cast",
                            default_index=0,
                            orientation="horizontal",
                    # with st.sidebar:
        
                            styles={
                                "container":{"padding": "0!important", "backgroubd-color":"red"},
                                "icon": {"color":"orange", "font-size": "10px"},
                                "nav-link":{
                                "font-size": "10px",
                                "text-align": "center",
                                "margin": "0px",
                                "--hover-color": "#eee",
                                },
                            "nav-link-selected":{"background-color": "green"},
                            },
                        )     
                if rad1 == "Total Runs":         
                        if len(df_selection2) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p0 = px.bar(
                                x=df_selection2["Total_Runs"],  
                                y=df_selection2["name"],
                                orientation="h",
                                title="<b>Runs by players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection2["Total_Runs"]),
                                template="plotly_white"
                            )


                            runs_p_p0.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p0)
                            
                        if len(df_selection2) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection2["Total_Runs"],  
                                y=df_selection2["name"],
                                orientation="h",
                                title="<b>Runs by players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection2["Total_Runs"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection2) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection2["Total_Runs"],  
                                y=df_selection2["name"],
                                # orientation="h",
                                title="<b>Runs by players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)
                            
                            
                if rad1 == "Batting Average":         
                        if len(df_selection2) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p = px.bar(
                                x=df_selection2["Batting_Avg"],  
                                y=df_selection2["name"],
                                orientation="h",
                                title="<b>Batting Average of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection2["Batting_Avg"]),
                                template="plotly_white"
                            )


                            runs_p_p.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p)
                            
                        if len(df_selection2) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection2["Batting_Avg"],  
                                y=df_selection2["name"],
                                orientation="h",
                                title="<b>Batting Average of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection2["Batting_Avg"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection2) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection2["Batting_Avg"],  
                                y=df_selection2["name"],
                                # orientation="h",
                                title="<b>Batting Average of players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)
                            
                if rad1 == "Strike Rate":         
                        if len(df_selection2) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p = px.bar(
                                x=df_selection2["Strike_rate"],  
                                y=df_selection2["name"],
                                orientation="h",
                                title="<b>Strike Rate of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection2["Strike_rate"]),
                                template="plotly_white"
                            )


                            runs_p_p.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p)
                            
                        if len(df_selection2) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection2["Strike_rate"],  
                                y=df_selection2["name"],
                                orientation="h",
                                title="<b>Strike Rate of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection2["Strike_rate"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection2) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection2["Strike_rate"],  
                                y=df_selection2["name"],
                                # orientation="h",
                                title="<b>Strike Rate of players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)
                
                
                if rad1 == "Wickets":         
                        if len(df_selection2) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p = px.bar(
                                x=df_selection2["wickets"],  
                                y=df_selection2["name"],
                                orientation="h",
                                title="<b>Wickets by players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection2["wickets"]),
                                template="plotly_white"
                            )


                            runs_p_p.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p)
                            
                        if len(df_selection2) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection2["wickets"],  
                                y=df_selection2["name"],
                                orientation="h",
                                title="<b>Wickets by players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection2["wickets"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection2) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection2["wickets"],  
                                y=df_selection2["name"],
                                # orientation="h",
                                title="<b>Wickets by players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)           

                            
                if rad1 == "Bowling Strike Rate":         
                        if len(df_selection2) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p = px.bar(
                                x=df_selection2["Bowling_Strike_Rate"],  
                                y=df_selection2["name"],
                                orientation="h",
                                title="<b>Bowling Strike Rate of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection2["Bowling_Strike_Rate"]),
                                template="plotly_white"
                            )


                            runs_p_p.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p)
                            
                        if len(df_selection2) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection2["Bowling_Strike_Rate"],  
                                y=df_selection2["name"],
                                orientation="h",
                                title="<b>Bowling Strike Rate of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection2["Bowling_Strike_Rate"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection2) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection2["Bowling_Strike_Rate"],  
                                y=df_selection2["name"],
                                # orientation="h",
                                title="<b>Bowling Strike Rate of players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)
                            
                            
                if rad1 == "Economy":         
                        if len(df_selection2) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p = px.bar(
                                x=df_selection2["Economy"],  
                                y=df_selection2["name"],
                                orientation="h",
                                title="<b>Economy of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection2["Economy"]),
                                template="plotly_white"
                            )


                            runs_p_p.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p)
                            
                        if len(df_selection2) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection2["Economy"],  
                                y=df_selection2["name"],
                                orientation="h",
                                title="<b>Economy of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection2["Economy"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection2) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection2["Economy"],  
                                y=df_selection2["name"],
                                # orientation="h",
                                title="<b>Economy of players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)
                
    if rad =="Finishers":
            # To display table
                data3 = pd.read_csv("Finishers.csv")
                st.sidebar.header("Please Filter Here: ")
                p_t3= st.sidebar.multiselect("Select the Team: ",
                                    options=data3["team"].unique(), 
                                    default=[data3["team"].iloc[60]])
                 
                p_bp3 = st.sidebar.multiselect("Select the Batting Position: ",
                                    options=data3["Batting_Position"].unique(), 
                                    default=[data3["Batting_Position"].unique()[7]])

                p_br3 = st.sidebar.multiselect("Select the Total Innings Batted: ", 
                                    options=data3["Total_Innings_Batted"].unique(), 
                                    default=[data3["Total_Innings_Batted"].unique()[0]])
                
                df_selection3 = data3.query(
                                  "team == @p_t3 & Batting_Position == @p_bp3 & Total_Innings_Batted == @p_br3"
                    )   
                st.dataframe(df_selection3)
                
                
                rad1 = option_menu(
                            menu_title="Graphical Representation",
                            options=["Total Runs","Batting Average", "Strike Rate","Wickets", "Bowling Strike Rate", "Economy"],
                            icons=["none","none","none","none","none", "none", "none", "none"],
                            menu_icon="cast",
                            default_index=0,
                            orientation="horizontal",
                    # with st.sidebar:
        
                            styles={
                                "container":{"padding": "0!important", "backgroubd-color":"red"},
                                "icon": {"color":"orange", "font-size": "10px"},
                                "nav-link":{
                                "font-size": "10px",
                                "text-align": "center",
                                "margin": "0px",
                                "--hover-color": "#eee",
                                },
                            "nav-link-selected":{"background-color": "green"},
                            },
                        ) 
                
                if rad1 == "Total Runs":         
                        if len(df_selection3) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p0 = px.bar(
                                x=df_selection3["Total_Runs"],  
                                y=df_selection3["name"],
                                orientation="h",
                                title="<b>Runs by players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection3["Total_Runs"]),
                                template="plotly_white"
                            )


                            runs_p_p0.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p0)
                            
                        if len(df_selection3) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection3["Total_Runs"],  
                                y=df_selection3["name"],
                                orientation="h",
                                title="<b>Runs by players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection3["Total_Runs"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection3) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection3["Total_Runs"],  
                                y=df_selection3["name"],
                                # orientation="h",
                                # title="<b>Runs by players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)
                            
                            
                if rad1 == "Batting Average":         
                        if len(df_selection3) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p = px.bar(
                                x=df_selection3["Batting_Avg"],  
                                y=df_selection3["name"],
                                orientation="h",
                                title="<b>Batting Average of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection3["Batting_Avg"]),
                                template="plotly_white"
                            )


                            runs_p_p.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p)
                            
                        if len(df_selection3) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection3["Batting_Avg"],  
                                y=df_selection3["name"],
                                orientation="h",
                                title="<b>Batting Average of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection3["Batting_Avg"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection3) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection3["Batting_Avg"],  
                                y=df_selection3["name"],
                                # orientation="h",
                                title="<b>Batting Average of players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)
                            
                if rad1 == "Strike Rate":         
                        if len(df_selection3) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p = px.bar(
                                x=df_selection3["Strike_rate"],  
                                y=df_selection3["name"],
                                orientation="h",
                                title="<b>Strike Rate of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection3["Strike_rate"]),
                                template="plotly_white"
                            )


                            runs_p_p.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p)
                            
                        if len(df_selection3) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection3["Strike_rate"],  
                                y=df_selection3["name"],
                                orientation="h",
                                title="<b>Strike Rate of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection3["Strike_rate"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection3) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection3["Strike_rate"],  
                                y=df_selection3["name"],
                                # orientation="h",
                                title="<b>Strike Rate of players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)
                
                
                if rad1 == "Wickets":         
                        if len(df_selection3) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p = px.bar(
                                x=df_selection3["wickets"],  
                                y=df_selection3["name"],
                                orientation="h",
                                title="<b>Wickets by players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection3["wickets"]),
                                template="plotly_white"
                            )


                            runs_p_p.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p)
                            
                        if len(df_selection3) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection3["wickets"],  
                                y=df_selection3["name"],
                                orientation="h",
                                title="<b>Wickets by players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection3["wickets"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection3) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection3["wickets"],  
                                y=df_selection3["name"],
                                # orientation="h",
                                title="<b>Wickets by players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)           

                            
                if rad1 == "Bowling Strike Rate":         
                        if len(df_selection3) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p = px.bar(
                                x=df_selection3["Bowling_Strike_Rate"],  
                                y=df_selection3["name"],
                                orientation="h",
                                title="<b>Bowling Strike Rate of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection3["Bowling_Strike_Rate"]),
                                template="plotly_white"
                            )


                            runs_p_p.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p)
                            
                        if len(df_selection3) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection3["Bowling_Strike_Rate"],  
                                y=df_selection3["name"],
                                orientation="h",
                                title="<b>Bowling Strike Rate of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection3["Bowling_Strike_Rate"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection3) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection3["Bowling_Strike_Rate"],  
                                y=df_selection3["name"],
                                # orientation="h",
                                title="<b>Bowling Strike Rate of players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)
                            
                            
                if rad1 == "Economy":         
                        if len(df_selection3) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p = px.bar(
                                x=df_selection3["Economy"],  
                                y=df_selection3["name"],
                                orientation="h",
                                title="<b>Economy of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection3["Economy"]),
                                template="plotly_white"
                            )


                            runs_p_p.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p)
                            
                        if len(df_selection3) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection3["Economy"],  
                                y=df_selection3["name"],
                                orientation="h",
                                title="<b>Economy of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection3["Economy"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection3) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection3["Economy"],  
                                y=df_selection3["name"],
                                # orientation="h",
                                title="<b>Economy of players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)
            
    if rad =="Bowlers":
            # To display table
                data4 = pd.read_csv("Bowlers.csv")
                st.sidebar.header("Please Filter Here: ")
                p_t4= st.sidebar.multiselect("Select the Team: ",
                                    options=data4["team"].unique(), 
                                    default=[data4["team"].iloc[12]])
                 
                p_bs4 = st.sidebar.multiselect("Select the Bowling Style: ",
                                    options=data4["bowlingStyle"].unique(), 
                                    default=[data4["bowlingStyle"].unique()[6]])

                p_br4 = st.sidebar.multiselect("Select the Total Innings Bowled: ", 
                                    options=data4["Total_Innings_Bowled"].unique(), 
                                    default=[data4["Total_Innings_Bowled"].unique()[6]])
                
                df_selection4 = data4.query(
                                  "team == @p_t4 & bowlingStyle == @p_bs4 & Total_Innings_Bowled == @p_br4"
                    )   
                st.dataframe(df_selection4)
                
                rad1 = option_menu(
                            menu_title="Graphical Representation",
                            options=["Wickets", "Bowling Strike Rate", "Bowling Average", "Runs Conceded","Economy"],
                            icons=["none","none","none","none","none", "none"],
                            menu_icon="cast",
                            default_index=0,
                            orientation="horizontal",
                    # with st.sidebar:
        
                            styles={
                                "container":{"padding": "0!important", "backgroubd-color":"red"},
                                "icon": {"color":"orange", "font-size": "10px"},
                                "nav-link":{
                                "font-size": "10px",
                                "text-align": "center",
                                "margin": "0px",
                                "--hover-color": "#eee",
                                },
                            "nav-link-selected":{"background-color": "green"},
                            },
                        )    
                
                
                if rad1 == "Wickets":         
                        if len(df_selection4) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p = px.bar(
                                x=df_selection4["wickets"],  
                                y=df_selection4["name"],
                                orientation="h",
                                title="<b>Wickets by players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection4["wickets"]),
                                template="plotly_white"
                            )


                            runs_p_p.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p)
                            
                        if len(df_selection4) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection4["wickets"],  
                                y=df_selection4["name"],
                                orientation="h",
                                title="<b>Wickets by players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection4["wickets"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection4) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection4["wickets"],  
                                y=df_selection4["name"],
                                # orientation="h",
                                title="<b>Wickets by players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)           

                            
                if rad1 == "Bowling Strike Rate":         
                        if len(df_selection4) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p = px.bar(
                                x=df_selection4["Bowling_Strike_Rate"],  
                                y=df_selection4["name"],
                                orientation="h",
                                title="<b>Bowling Strike Rate of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection4["Bowling_Strike_Rate"]),
                                template="plotly_white"
                            )


                            runs_p_p.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p)
                            
                        if len(df_selection4) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection4["Bowling_Strike_Rate"],  
                                y=df_selection4["name"],
                                orientation="h",
                                title="<b>Bowling Strike Rate of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection4["Bowling_Strike_Rate"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection4) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection4["Bowling_Strike_Rate"],  
                                y=df_selection4["name"],
                                # orientation="h",
                                title="<b>Bowling Strike Rate of players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)
                
                if rad1 == "Bowling Average":         
                        if len(df_selection4) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p = px.bar(
                                x=df_selection4["bowling_Average"],  
                                y=df_selection4["name"],
                                orientation="h",
                                title="<b>Bowling Average of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection4["bowling_Average"]),
                                template="plotly_white"
                            )


                            runs_p_p.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p)
                            
                        if len(df_selection4) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection4["bowling_Average"],  
                                y=df_selection4["name"],
                                orientation="h",
                                title="<b>Bowling Average of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection4["bowling_Average"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection4) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection4["bowling_Average"],  
                                y=df_selection4["name"],
                                # orientation="h",
                                title="<b>Bowling Average of players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)           
                            
                if rad1 == "Runs Conceded":         
                        if len(df_selection4) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p = px.bar(
                                x=df_selection4["Runs_Conceded"],  
                                y=df_selection4["name"],
                                orientation="h",
                                title="<b>Runs Conceded by players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection4["Runs_Conceded"]),
                                template="plotly_white"
                            )


                            runs_p_p.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p)
                            
                        if len(df_selection4) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection4["Runs_Conceded"],  
                                y=df_selection4["name"],
                                orientation="h",
                                title="<b>Runs Conceded by players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection4["Runs_Conceded"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection4) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection4["Runs_Conceded"],  
                                y=df_selection4["name"],
                                # orientation="h",
                                title="<b>Runs Conceded by players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)
                            
                if rad1 == "Economy":         
                        if len(df_selection4) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p = px.bar(
                                x=df_selection4["Economy"],  
                                y=df_selection4["name"],
                                orientation="h",
                                title="<b>Economy of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection4["Economy"]),
                                template="plotly_white"
                            )


                            runs_p_p.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p)
                            
                        if len(df_selection4) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p01 = px.line(
                                x=df_selection4["Economy"],  
                                y=df_selection4["name"],
                                orientation="h",
                                title="<b>Economy of players</b>",
                                color_discrete_sequence=["#0083B8"] * len(df_selection4["Economy"]),
                                template="plotly_white"
                            )


                            runs_p_p01.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p01)
                            
                        if len(df_selection4) == 0:
                            st.warning("No data found with the selected filters.")
                        else:
                            runs_p_p02 = px.scatter(
                                x=df_selection4["Economy"],  
                                y=df_selection4["name"],
                                # orientation="h",
                                title="<b>Economy of players</b>",
                                height=400, width=600,
                                # mode='markers',
                                # marker=dict(
                                # color=[120, 125, 130, 135, 140, 145],
                                # size=[15, 30, 55, 70, 90, 110],
                                # showscale=True
                                # )
                            )


                            runs_p_p02.update_layout(
                                plot_bgcolor="rgba(0,0,0,0)",
                                xaxis=dict(showgrid=False)
                            )

                            st.plotly_chart(runs_p_p02)
            
    if rad == "Make your team":
            

            # Read CSV file and store the data in a list of dictionaries
        

            with open('Finishers.csv') as csvfile:
                players = list(csv.DictReader(csvfile))

            # Create a pandas DataFrame to store the added players
            df = pd.DataFrame(columns=players[0].keys())

            
            st.write("Criteria for selection:")
            st.write("5 Batsmans, 1 Wicket-Keeper & 5 Bowlers")
            # st.write("1 Wicket-Keeper")
            # st.write("5 Bowlers")
            # Take user input as a query
            query = st.text_input("Enter player name to search: ")

            # Search for the player in the list of dictionaries
            player_found = False
            for player in players:
                if player is not None and player.get('ï»¿name') is not None and player.get('ï»¿name').lower() == query.lower():
                    # Display the player details
                    st.write("Player Found")
                    st.write(player)
                    player_found = True
                    break

            # If player is not found, display an error message
            if not player_found:
                st.write("Player not found in the list.")
            df01 = pd.read_csv('file.csv')
            # Define the add function to add players to the DataFrame
            def add_player(player):
                    global df, df01
                    
                    df = df.append(player, ignore_index=True)
                    df01 = pd.concat([df01, df], ignore_index=True)
                    df01.to_csv('file.csv', index=False)
                    st.write("Player added successfully!")
                    st.write(df01)


            # Call the add function on button click
            if st.button("Add Player"):
                if player_found:
                    add_player(player)
                else:
                    st.write("Cannot add player as it was not found in the list.")
            
            # df01 = pd.read_csv('file.csv')        
            # def delete_player(query):
            #     global df, df01
            #     new_df = df.drop(df[df['ï»¿name'].str.lower() == query.lower()].index)
            #     df = new_df.copy()
            #     df01 = pd.concat([df01,df], ignore_index=True)
            #     df01.to_csv('file.csv', index=False)
            #     st.write("Player deleted successfully!")            
            #     st.write(df01)

            # if st.button("Delete Player"):
            #     if player_found:
            #         delete_player(query)
            #     else:
            #         st.write("Cannot delete player as it was not found in the list.")

            df = pd.read_csv('file.csv')

# Add a button to download the data as an Excel file
            if st.button('View the list'):
                # Set the filename and type of file
                filename = 'Final11.xlsx'
                file_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                d = pd.read_csv("file.csv")
                st.dataframe(d)
    
    # Configure the response headers
                headers = {
                    'Content-Disposition': f'attachment; filename="{filename}"',
                    'Content-Type': file_type,
                }
    
                # Write the CSV data to an Excel file
                with st.spinner('Downloading...'):
                    output = io.BytesIO()
                    writer = pd.ExcelWriter(output, engine='xlsxwriter')
                    df.to_excel(writer, index=False, sheet_name='Sheet1')
                    writer.save()
                    output.seek(0)
                    st.write('Download the file from the following link:')
                    st.download_button(label='Download the list', data=output.read(), file_name=filename, mime=file_type)
                    # st.success('Download complete!')


    elif authentication_status is False:
        st.error('Username/password is incorrect')
    elif authentication_status is None:
        st.warning('Please enter your username and password')

  
