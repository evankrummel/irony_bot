#AttributeError: 'ClientUser' object has no attribute 'send'
#attempting to send to itself dispite if clause?

#attachments?

#format final


import discord
import asyncio
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

#submit
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
    user = client.get_channel(813872172799754250)
    forward = f"`{client.user.name}` is online!"
    await user.send(forward)
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="over the server!"))

@client.event
async def on_message(message):
    if message.author.id != client.user.id:
        if message.guild is None:
            modnotice = client.get_channel(813872172799754250)
            forward = f"User `{message.author.name}` said: ```{message.content}```"
            await modnotice.send(forward)
            if message.author not in session:
#Session Restart
                if "$session" in message.content.lower():
                    await message.author.send("Restarting Session")
                    session.clear()
                    print("Session Restarted")
                else:
#Main Menu
                    await message.author.send(r1)
                    session.append(message.author)
                    try:
                        message = await client.wait_for("message", timeout=60.0)
                    
                    except asyncio.TimeoutError:
                            await message.channel.send(to1)
                            session.remove(message.author)
#Submission Line 1
                    else:
                        if "submit" in message.content.lower() or "submission" in message.content.lower():
                            await message.author.send(r2s)
                            user = client.get_channel(813872172799754250)
                            submitnotice = f"User `{message.author.name}` is submitting an assignment! <@&806274913904230410>"
                            await user.send(submitnotice)
                            
                            def check(m):
                                return user == message.author
                            
                            try:
                                message = await client.wait_for("message", timeout=60.0)
                                
                            except asyncio.TimeoutError:
                                    await message.channel.send(to1)
                                    session.remove(message.author)
                            
#Submission Line 2 (Class Number)
                            else:
                                if "1" in message.content.lower() or "2" in message.content.lower() or "3" in message.content.lower() or "4" in message.content.lower() or "5" in message.content.lower() or "6" in message.content.lower() or "7" in message.content.lower() or "8" in message.content.lower() or "9" in message.content.lower():
                                    await message.author.send(r3s)
                                    
                                    def check(m):
                                        return user == message.author
                                    
                                    try:
                                        message = await client.wait_for("message", timeout=60.0)
                                        
                                    except asyncio.TimeoutError:
                                        await message.channel.send("to1")
                                        session.remove(message.author)
#Submission Line 3 (Assignment Name)
                                    else:
                                        await message.author.send(r4s)
                                        
                                        def check(m):
                                            return user == message.author
                                        
                                        try:
                                            message = await client.wait_for("message", timeout=60.0)
                                            
                                        except asyncio.TimeoutError:
                                                await message.channel.send(to1)
                                                session.remove(message.author)
#Submission Line 4 (Include Tag)
                                        else:
                                            if "yes" in message.content.lower() or "sure" in message.content.lower() or "yep" in message.content.lower() or "yeah" in message.content.lower():
                                                await message.author.send(r5s)
                                                
                                                def check(m):
                                                    return user == message.author
                                                
                                                try:
                                                    message = await client.wait_for("message", timeout=60.0)
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
                                                    return user == message.author

                                                try:
                                                    message = await client.wait_for("message", timeout=60.0)
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
                    print('Meme Posted:')
                    user = client.get_channel(813872172799754250)
                    forward = f"User `{message.author.name}` Posted a Meme."
                    await user.send(forward)
                    print('Origin: ', message.author.name)
                    print(' -- ')

@client.command()
async def start(ctx):
    print("test")
    session.remove(ctx.author)
    await ctx.send("System Reset Complete")

client.run('ODExOTg4ODgxNzEzMDA0NjA0.YC6Nkw.CcJarZHBMINsq7D2F64MvUJx8tA')