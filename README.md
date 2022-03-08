# wowproject
The effect of social interaction on  individual churn decision in Game

- Introduction 

This repository is for my thesis project code, " The effect of social interaction on  individual churn decision in Game "

Churn prediction in game is complicated because it’s uneasy to catch the point from where players start feel bored and decide to leave. However, we could think what makes game fun to them, who or what the users are interacting with. Game design includes not only human-computer interaction but also between users’ interaction. Especially in the MMORPG game, game designers devise means to increase the social interaction among users. They make quests which are impossible clear alone, team confrontations events, inner communities like ‘guild’. These create ‘peer effect’ to continue to play but it’s not enough explanation. It’s better to see social interaction itself is one of the fun factors of game.    

Since everyone has different intrinsic motivation for game, the impact of social interaction on individuals’ fun would be different. According to self-determination theory, autonomy and competence are two intrinsic motivations contributing to absorbing in game. This can be found in other quantitative marketing research.  (Nevskaya & Albuquerque, 2019; Zhao, Yang, Shum, & Dut, 2022) divided user type into‘achiever’and‘experiencer’, grouping those who respond to external rewards more as ‘achiever’. Those who value competence and those who value autonomy will be influenced by social interaction differently, and this would affect on individual’s decision to leave the game. 

In this research, 1) I’d like to analyze that how social interaction factors impacts on individual churn decision according to the user type. 2) With user type and other social interaction factors, we could predict the possibility of leaving the game in week t at individual level. 3) As a result, this research would find out the relationship contribute to making social interacting events or marking policy for decreasing churn rate considering user groups in the game and other industry.   



- Data

For data, (Lee, Chen, Lei, & Cheng, 2011) provided the user log data of the famous MMORPG, World of Warcraft. I chose to use the log data of 52 weeks (1 year), from April 2007 to March of 2008. It’s a period far from the between new game season patches (January 2007 and November 2008) which is enough to avoid the effect of the patches. 

Also, 2007 patch update introduced “Players vs Players (Pvp)” contents, which provides arenas to fight with other teams. In arena, players forming their teams (from 2~3 players) and fight for items that other team owns. This content offers chance to make social interaction stronger and build group identity.  

The object group of research is the avatars that starts game in that period (starting level 1~3), those who I could trace time records for their level up process. It’s because that the behavioral pattern for level up process is the crucial evidence to discriminate the user type. 
In the dataset, the 9,232 avatars were selected, and 313,954 observation records were made for research. Among these, 2000 avatars were discriminated as test data id (68,018 records) and 7,232 avatars belonged to train data(245,936 records).  Each records contains avatar id, guild id, type of user (X_i) weekly playtime, guild size (B_it), whether their playtime is over weekly average (W_it), cumulated experience of Pvp (C_it), cumulated number of guild change (D_it), successive week records of not gaming.

The Data is open-source data and can be downloaded freely from below: 
 http://mmnet.iis.sinica.edu.tw/dl/wowah/


