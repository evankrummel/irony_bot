#This bot was commissioned by RandomStudent and created by Evan Krummel with help from Hidd.  No money changed hands in the creation of the bot.
#If you want to support the development of the bot, you can donate to the mod team via ETH Wallet 0x60b06AF47AB3E100403732f2f804944234Fa4870

import discord
import asyncio
import string
import random
import secrets
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
session = []

#Main Menu
r1l1 = "Hey!  I'm a bot that can help you with anything related to the Ironic server.  What can I help you with?  Please choose one of the following:"
r1l2 = ":mailbox: Submission; If you have an assignment to submit, you can do that here!"
r1l3 = ":books: Join/Leave Class; If you want to join/leave a class, you can do that here!"
r1l4 = ":white_check_mark: Correction; If you noticed a mistake in a submission, you can correct them here!"
r1l5 = ":wrench: Help; If you need anything else, that can be resolved here!"
r1l6 = "You can respond with a similar word, or the according emote.  If you get lost in the directory at any point, you can type !help to request help from a moderator.  You can also type !start at any point to go back to this first directory."
r1 = f"{r1l1} \n {r1l2} \n {r1l3} \n {r1l4} \n {r1l5} \n {r1l6}"

#Submit
r2s = ":partying_face: Awesome, thanks for contributing to the community!  What class is this for?  Please respond using the class number (1-15)."
r3s = ":pencil2: Great!  What is this assignment called?"
r4s = ":mega: Ok, got it.  Would you like your handle attached to the submission?  This will let everyone know who submitted the assignment."
r5s = ":notepad_spiral: Do you want to attach any sort of note to the assignment? This can be something describing your thought process, explaining a question, or even letting people know that you're not so sure about a given question. (If yes, simply reply with your note.  Otherwise, say `no`)"
r6s = ":camera_with_flash: Nice.  You can now send photos/files of the assignment.  When you're done sending them, say `done`."

#Join/Leave Class
r2jl = ":book: If you need to join or leave classes, I can help you with that!  Which one would you like to do?"

#Join Class
r2j = f":books: Ok, we currently support the following classes.  Which ones would you like to join? \n 1 - DP Visual Arts (Whittle) \n 2 - DP History (VanGoor) \n 3 - Spanish V (Castillo) \n 4 - AA Mathematics (Vecziedins) \n 5 - DP Biology (Thane) \n 6 - DP English (Donohue) \n 7 - DP Chemistry (Vogl) \n 8 - Chinese V (Beckwith) \n 9 - AI Mathematics (Burke) \n 10 - DP ESS (Rizley) \n 11 - DP History (Stachura) \n 12 - Music Theory (Jeroudi) \n 13 - TOK (Global) \n 14 - EPIC (Global) \n 15 - Psychology (Miller) \n Respond with the class number. "
r3j = ":file_cabinet:  Sounds good!  I'll have a moderator update your roles right away.  If you need anything else, just say so!"

#Leave Class
r2l = f":bookmark: Sure, which class(es) would you like to leave?  Please respond with the class number. \n 1 - DP Visual Arts (Whittle) \n 2 - DP History (VanGoor) \n 3 - Spanish V (Castillo) \n 4 - AA Mathematics (Vecziedins) \n 5 - DP Biology (Thane) \n 6 - DP English (Donohue) \n 7 - DP Chemistry (Vogl) \n 8 - Chinese V (Beckwith) \n 9 - AI Mathematics (Burke) \n 10 - DP ESS (Rizley) \n 11 - DP History (Stachura) \n 12 - Music Theory (Jeroudi) \n 13 - TOK (Global) \n 14 - EPIC (Global) \n 15 - Psychology (Miller) \n Respond with the class number. "
r3l = ":file_cabinet:  Sounds good!  I'll have a moderator update your roles right away.  If you need anything else, just say so!"

#Correction
r2c = ":wave: Hey!  If you found a mistake in a submission, I can help rollout a correction! Your discord handle will be attached to any corrections you make. What class did you notice a error in?"
r3c = ":thumbsup: Got it.  What is the Assignment ID?"
r4c = ":hash: Great!  What question number, section, etc. did you notice the mistake in?  Put this in your own words, since assignments can be different in their structure.  We'll ask you the specifics of the error next."
r5c = ":woman_detective: Sounds good.  What was the error you noticed?  Please go into as much detail as possible, and include your corrected answer."
r6c = ":star_struck: Awesome!  I'll ping a moderator to check over your correction ticket now.  If they need any more information, they might follow up with you.  We'll let you know when your correction has been posted!"

#Help / Other
r2hl1 = "What can I help you with?"
r2hl2 = ":one: Ping a Moderator."
r2hl3 = ":two: View Developer Notes"
r2h = f"{r2hl1} \n {r2hl2} \n {r2hl3}"
r3hp1 = ":cowboy: I'll ping a moderator now.  If there aren't any online at the moment, I'll have them follow up with you later."

#Dev Notes
r2hd1l1 = "Welcome to the developer notes."
r2hd1l2 = "This bot was commissioned by RandomStudent and created by Evan Krummel with help from Hidd.  No money changed hands in the creation of the bot."
r2hd1l3 = "You can view the following info:"
r2hd1l4 = ":one: Bot Map"
r2hd1l5 = ":two: Usage Notes"
r2hd1l6 = ":three: Changelog"
r2hd1l7 = "Respond with the exact words above, excluding the emote.  Saying anything else will bring you back to the main menu."
r2hd1 = f"{r2hd1l1} \n {r2hd1l2} \n \n {r2hd1l3} \n {r2hd1l4} \n {r2hd1l5} \n {r2hd1l6} \n {r2hd1l7}"

#Error
to1 = ":sob: This conversation has timed out due to inactivity.  Saying anything will start you back at the main menu."
e1 = ":face_with_raised_eyebrow: Sorry, I'm not sure I understand what you mean.  Could you try again in different words?"
e2 = ":woman_detective: If you're having trouble with the bot, feel free to reach out to a moderator personally with your issue."

client = commands.Bot(command_prefix='!', intents=intents)
@client.event
async def on_ready():
    print(f"{client.user.name} is online!")
    user = client.get_channel(822482846119231536)
    forward = f"`{client.user.name}` is online!"
    await user.send(forward)
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="over the server!"))

@client.event
async def on_message(message):
    if message.author.id != client.user.id:
#Session Restart
        if "$session" in message.content.lower():
            await message.author.send("Restarting Session")
            session.clear()
            print("Session Restarted")
        else:
            if message.guild is None:
                channel = client.get_channel(813872172799754250)
                forward = f"User `{message.author.name}` said: ```{message.content}```"
                await channel.send(forward)
                if message.author not in session:
#Main Menu
                    await message.author.send(r1)
                    session.append(message.author)
            
                    def check(m):
                        return client.user.id != message.author.id
                    
                    try:
                        message = await client.wait_for("message", timeout=60.0, check=check)
                    
                    except asyncio.TimeoutError:
                            await message.channel.send(to1)
                            session.remove(message.author)
#Submission Line 1
                    else:
                        if "submit" in message.content.lower() or "submission" in message.content.lower():
                            await message.author.send(r2s)
                            channel = client.get_channel(813872172799754250)
                            submitnotice = f"User `{message.author.name}` is submitting an assignment! <@&806274913904230410>"
                            await channel.send(submitnotice)
                            
                            def check(m):
                                return client.user.id != message.author.id
                            
                            try:
                                message = await client.wait_for("message", timeout=60.0, check=check)
                                
                            except asyncio.TimeoutError:
                                    await message.channel.send(to1)
                                    session.remove(message.author)
#Submission Line 2 (Class Number)
                            else:
                                if "1" in message.content.lower() or "2" in message.content.lower() or "3" in message.content.lower() or "4" in message.content.lower() or "5" in message.content.lower() or "6" in message.content.lower() or "7" in message.content.lower() or "8" in message.content.lower() or "9" in message.content.lower():
                                    await message.author.send(r3s)
                                    
                                    def check(m):
                                        return client.user.id != message.author.id
                                    
                                    try:
                                        message = await client.wait_for("message", timeout=60.0, check=check)
                                        
                                    except asyncio.TimeoutError:
                                        await message.channel.send("to1")
                                        session.remove(message.author)
#Submission Line 3 (Include Tag)
                                    else:
                                        await message.author.send(r4s)
                                        
                                        def check(m):
                                            return client.user.id != message.author.id
                                        
                                        try:
                                            message = await client.wait_for("message", timeout=60.0, check=check)
                                        except asyncio.TimeoutError:
                                                await message.channel.send(to1)
                                                session.remove(message.author)
#Submission Line 4 (Note)
                                        else:
                                            if "yes" in message.content.lower() or "sure" in message.content.lower() or "yep" in message.content.lower() or "yeah" in message.content.lower():
                                                await message.author.send(r5s)
                                                
                                                def check(m):
                                                    return client.user.id != message.author.id
                                                
                                                try:
                                                    message = await client.wait_for("message", timeout=60.0, check=check)
                                                except asyncio.TimeoutError:
                                                        await message.channel.send(to1)
                                                        session.remove(message.author)
#Submission Line 5 *Tag Included* *No Note* (Attachments)
                                                else:
                                                    if "no" in message.content.lower():
                                                        await message.author.send("Yes Tag, No Note")
                                                        session.remove(message.author)
#Submission Line 5 *Tag Included* *Yes Note* (Attachments)
                                                    else:
                                                        await message.author.send("Yes Tag, Yes Note")
                                                        session.remove(message.author)
#Submission Line 5 *No Tag* (Note)
                                            elif "no" in message.content.lower() or "nah" in message.content.lower() or "nope" in message.content.lower():
                                                await message.author.send(r5s)
                                                
                                                def check(m):
                                                    return client.user.id != message.author.id

                                                try:
                                                    message = await client.wait_for("message", timeout=60.0, check=check)
                                                except asyncio.TimeoutError:
                                                    await message.channel.send(to1)
                                                    session.remove(message.author)
#Submission Line 5 *No Tag* *No Note* (Attachments)
                                                else:
                                                    if "no" in message.content.lower():
                                                        print("No Tag, No Note")
                                                        await message.author.send("No Tag, No Note")
                                                        session.remove(message.author)
#Submission Line 5 *No Tag* *Yes Note* (Attachments)
                                                    else:
                                                        print("final 2")
                                                        await message.author.send("No Tag, Yes Note")
                                                        session.remove(message.author)
#Errors
                                            else:
                                                await message.author.send(e1)
                                                await message.author.send(e2)
                                                session.remove(message.author)
                                else:
                                    await message.author.send(e1)
                                    await message.author.send(e2)
                                    session.remove(message.author)
                        
#Line
                        elif "join class" in message.content.lower():
                            await message.author.send("Test 1 Passed")
                            session.remove(message.author)
                            
                        elif "leave class" in message.content.lower():
                            await message.author.send("Test 2 Passed")
                            session.remove(message.author)
                            
                        elif "join/leave" in message.content.lower():
                            await message.author.send("Test 3 Passed")
                            session.remove(message.author)
                            
                        elif "correct" in message.content.lower() or "correction" in message.content.lower():
                            await message.author.send("Test 4 Passed")
                            session.remove(message.author)
                            
                        elif "help" in message.content.lower():
                            await message.author.send(r2h)
                            session.remove(message.author)
                            
                        elif "$session" in message.content.lower():
                            await message.author.send("Restarting Session")
                            session.clear()
                            
                        else:
                            await message.author.send(e1)
                            await message.author.send(e2)
                            session.remove(message.author)
#Meme Response
            else:
                if message.channel == client.get_channel(808452909367820288):
                    if message.attachments:
                        await message.add_reaction("<:good_meme:808824921484558348>")
                        await message.add_reaction("<:bad_meme:808826207361695786>")
                        numbo = secrets.token_hex(14)
                        modchannel = client.get_channel(822479640492507176)
                        forward = f"User `{message.author.name}` Just Posted a Meme!  ID: `0x{numbo}`"
                        await modchannel.send(forward)
                elif message.channel == client.get_channel(822602852609687552):
                    if "assignment title" in message.content.lower() and "class" in message.content.lower() and "submission type" in message.content.lower() and "user" in message.content.lower():
                        tokena = secrets.token_hex(30)
                        await message.add_reaction("<:good_meme:808824921484558348>")
                        await message.channel.send(":white_check_mark: Section 1 Clear", delete_after=3)
                        await message.channel.send(":white_check_mark: Section 2 Clear", delete_after=3)
                        await message.channel.send(":white_check_mark: Section 3 Clear", delete_after=3)
                        await message.channel.send(":white_check_mark: Section 4 Clear", delete_after=3)
                        await message.channel.send(":ballot_box_with_check: Transaction has been cleared to T1.  Awaiting crowdsourced verification for T2.", delete_after=5)
                        await message.author.send(f":hash: Your Post ID is `0x{tokena}`")
                        forwardchannel = client.get_channel(822618074548535378)
                        forward = f"`{message.author.name}` submitted a post query. \n ID: `0x{tokena}`"
                        await forwardchannel.send(forward)
                        
                    else:
                        if "assignment title" in message.content.lower():
                            await message.channel.send(":white_check_mark: Section 1 Clear", delete_after=3)
                            if "class" in message.content.lower():
                                await message.channel.send(":white_check_mark: Section 2 Clear", delete_after=3)
                                if "submission type" in message.content.lower():
                                    await message.channel.send(":white_check_mark: Section 3 Clear", delete_after=3)
                                    if "user" in message.content.lower():
                                        await message.channel.send(":white_check_mark: Section 4 Clear", delete_after=3)
                                    else:
                                        await message.channel.send(":customs: **Section 4 Check Failed.**  Please edit and try again.", delete_after=5)
                                        await message.add_reaction("🛃")
                                else:
                                    await message.channel.send(":customs: **Section 3 Check Failed.**  Please edit and try again.", delete_after=5)
                                    await message.add_reaction("🛃")
                            else:
                                await message.channel.send(":customs: **Section 2 Check Failed.**  Please edit and try again.", delete_after=5)
                            await message.add_reaction("🛃")
                        else:
                            await message.channel.send(":customs: **Section 1 Check Failed.**  Please edit and try again.", delete_after=5)
                            await message.add_reaction("🛃")
                elif message.channel == client.get_channel(822624786030395412):
                    if "+1" in message.content.lower() and ";" in message.content.lower():
                        await message.channel.send(":white_check_mark: User Verified", delete_after=3)
                        await message.channel.send(":white_check_mark: Class Verified", delete_after=3)
                        await message.channel.send(":ballot_box_with_check: Submission cleared. Awaiting count.", delete_after=5)
                        await message.add_reaction("<:good_meme:808824921484558348>")
                    else:
                        await message.channel.send(":customs: There seems to be an error.  Please check your formatting and try again.", delete_after=5)
                        await message.add_reaction("🛃")

client.run('ODExOTg4ODgxNzEzMDA0NjA0.YC6Nkw.8U0ApCd8jov3NZY7ILtnL7L7Gzk')
