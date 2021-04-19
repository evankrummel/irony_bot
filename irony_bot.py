import discord
import asyncio
import string
import random
import secrets
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
session = []
submitattach = []
forwardattachments = []

#Main Menu
r1l1 = "Hey!  I'm a bot that can help you with anything related to the Ironic server.  What can I help you with?"
r1l2 = ":mailbox: Submission; If you have an assignment to submit, you can do that here!"
r1l3 = ":books: Join/Leave Class; If you want to join/leave a class, you can do that here!"
r1l4 = ":white_check_mark: Correction; If you noticed a mistake in a submission, you can correct them here!"
r1l5 = ":wrench: Help; If you need anything else, that can be resolved here!"
r1l6 = "You can respond with a similar word, or the according emote.  If you get lost in the directory, you can always type $start to restart your session."
r1 = f"{r1l1} \n {r1l2} \n {r1l3} \n {r1l4} \n {r1l5} \n {r1l6}"

#Submit
r2srand = [":partying_face: Cool!  What class is this for?  Please respond using the class number (1-15).", ":smiling_face_with_3_hearts: YOOOO thanks for contributing to the community!  What class do you want to submit to?  Please respond using the class number (1-15).", ":grin: Nice! What class is this for? Please respond using the class number (1-15).", ":cowboy: Woah, cool!  Thanks so much for contributing to the community! What class do you want to submit to?  Respond using the class number (1-15)."]
r3sp1rand = [":pencil2: Great, I'll post this assignment to ", ":star_struck: Sounds good, I'll post this submission to ", ":cowboy: Got it, I'll post this to ", ":smile_cat: Got it! I'll put post this to "]
r3sp2rand = ["What is this assignment called?", "What's the title of this assignment?", "What's this submission called?", "What should I title the submission?"]
r4soptions = [":mega: Ok, got it.  Would you like your handle attached to the submission?", ":cowboy: Now that's a groovy title!  Do you want your handle attached to the submission?", ":sunglasses: Cool, do you want your handle attached to the submission?"]
r5soptions = [":notepad_spiral: Okay, do you want to attach any sort of note to the assignment? If yes, simply reply with your note.  Otherwise, just say `no`.", ":pencil2: Sounds good.  Do you want to include any sort of note with your submission?  If yes, simply reply with your note.  Otherwise, just say `no`.", ":memo: Got it.  Do you want any sort of note included with your submission? If yes, simply reply with your note.  Otherwise, just say `no`.", ":cowboy: Got it.  Do you want to include any sort of note with your submission? If you do, simply reply with your note.  Otherwise, just say `no`."]
r6s = ":camera_with_flash: Nice.  You can now send photos of the assignment.  When you're done sending them, say `done` (Max. 5 Attachments, Don't include comments)."
r7s = ":tada: I'll have a moderator post this on #assignments as soon as possible.  Thanks again for your submission!"
r8s = ":+1: Here's what your submission looks like.  Is everything correct?"

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
to1options = [":sob: This conversation has timed out due to inactivity.  Saying anything will start you back at the main menu.", ":cry: Oh no!  This conversation has timed out due to inactivity.  Saying anything will trigger the main menu.", ":fearful: Agh!  Sorry, but the session has timed out.  Saying anything will send you back to the main menu.", ":cold_face: Welp, the conversation has timed out.  Saying anything will send you back to the main menu."]
to1 = random.choice(to1options)
e1 = ":face_with_raised_eyebrow: Sorry, I'm not sure I understand what you mean.  Could you try again in different words?"
e2 = ":woman_detective: If you're having trouble with the bot, feel free to reach out to a moderator personally with your issue."
ol3 = ":smiling_face_with_tear: Sorry, the bot can only accept up to 5 images at this time.  Please try again."
invalclass = [":woman_detective: Uhhhh sorry, that's not a valid class number.  Maybe try again?", ":confounded: Hmmm... that's not a valid class number.  Let's try again!", ":grimacing: Well, this is a bit awkward.  It doesn't seem like you've provided a valid class number.  Let's start over."]

#Clubs
clubsl1 = ":woman_guard: Here are the current active clubs:"
clubsl2 = "**Class 6** - *The Joy Luck Club* - `Meets on Wednesdays at 3:00PM`"
clubsl3 = "**Class 9** - *Math Study Club* - `Meets on Wednesdays at 1:00PM`"
clubs = f"{clubsl1} \n{clubsl2} \n{clubsl3}"
nullclub = ":confused: Sorry, this class doesn't have an active club at the moment.  Myabe try a different club, or you can type `$club ?` to view a list of all active clubs."
noclassclub = ":confused: Sorry, it looks like you haven't included a valid class number. Maybe try again? Or, you can type `$club ?` to view a list of all active clubs."
club9 = ":ballot_box_with_check: Great, we'll add you to The Math Study Club right away!"
club6 = ":ballot_box_with_check: Great, we'll add you to The Joy Luck Club right away!"

#Personalization
embedcoloroptions = ["0xffb5af", "0xa8c6fe", "0xb18cfe", "0xf4a4c0", "0x94e3fe", "0xb18cfe"]

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
    botforwards = client.get_channel(813872172799754250)
    if message.author.id != client.user.id:
        allforwardchannel = client.get_channel(822973502965284874)
        allforward = f"`{message.author.name}` said: ```{message.content}```"
        if message.guild is None:
            allforwardembed=discord.Embed(title=f"New Bot Interaction", description=f"<@811988881713004604>", color=0x74a7fe)
            allforwardembed.set_author(name=f"{message.author.name}", icon_url=f"{message.author.avatar_url}")
            if message.content:
                allforwardembed.add_field(name="Content:", value=f"{message.content}", inline=False)
            else:
                allforwardembed.add_field(name="Content:", value=f"No Message Included", inline=False)
            if message.attachments:
                allforwardembed.set_footer(text="Attachments included.")
            await allforwardchannel.send(embed=allforwardembed)
        else:
            allforwardembed=discord.Embed(title=f"New Server Message", description=f"{message.channel.mention}", color=0xe392fe)
            allforwardembed.set_author(name=f"{message.author.name}", icon_url=f"{message.author.avatar_url}")
            if message.content:
                allforwardembed.add_field(name="Content:", value=f"{message.content}", inline=False)
            else:
                allforwardembed.add_field(name="Content:", value=f"No Message Included", inline=False)
            if message.attachments:
                allforwardembed.set_footer(text="Attachments included.")
            await allforwardchannel.send(embed=allforwardembed)
#Session Restart
        if "$start" in message.content.lower():
            await message.author.send("Restarting Session")
            session.clear()
            print("Session Restarted")
        elif "$club" in message.content.lower():
            if "1" in message.content.lower():
                await message.author.send(nullclub)
            elif "2" in message.content.lower():
                await message.author.send(nullclub)
            elif "3" in message.content.lower():
                await message.author.send(nullclub)
            elif "4" in message.content.lower():
                await message.author.send(nullclub)
            elif "5" in message.content.lower():
                await message.author.send(nullclub)
            elif "6" in message.content.lower():
                await message.author.send(club6)
                botforwards = client.get_channel(813872172799754250)
                forward = f"`{message.author.name}` wants to join `Joy Luck Club - 6` <@&806274913904230410>"
                await botforwards.send(forward)
            elif "7" in message.content.lower():
                await message.author.send(nullclub)
            elif "8" in message.content.lower():
                await message.author.send(nullclub)
            elif "9" in message.content.lower():
                await message.author.send(club9)
                botforwards = client.get_channel(813872172799754250)
                forward = f"`{message.author.name}` wants to join `Math Study Club - 9` <@&806274913904230410>"
                await botforwards.send(forward)
            elif "10" in message.content.lower():
                await message.author.send(nullclub)
            elif "11" in message.content.lower():
                await message.author.send(nullclub)
            elif "12" in message.content.lower():
                await message.author.send(nullclub)
            elif "13" in message.content.lower():
                await message.author.send(nullclub)
            elif "14" in message.content.lower():
                await message.author.send(nullclub)
            elif "15" in message.content.lower():
                await message.author.send(nullclub)
            elif "?" in message.content.lower():
                await message.author.send(clubs)
            else:
                await message.author.send(noclassclub)
        else:
            if message.guild is None:
                if message.author not in session:
#Main Menu
                    await message.author.send(r1)
                    session.append(message.author)
                    submitattach = []
            
                    def check(m):
                        return client.user.id != m.author.id and reply1.guild is None and m.author == message.author
                    
                    try:
                        reply1 = await client.wait_for("message", timeout=60.0, check=check)
                    
                    except asyncio.TimeoutError:
                            await message.channel.send(to1)
                            session.remove(message.author)
#Submission Line 1
                    else:
                        if "submit" in reply1.content.lower() or "submission" in reply1.content.lower() or "📫" in reply1.content.lower() or "📪" in reply1.content.lower() or "📬" in reply1.content.lower() or "📭" in reply1.content.lower() or "\U0001f4ec" in reply1.content.lower() or "\U0001f4ea" in reply1.content.lower():
                            randclassname = random.choice(r2srand)
                            await reply1.author.send(randclassname)
                            
                            def check(m):
                                return client.user.id != m.author.id and m.guild is None and m.author == reply1.author
                            
                            try:
                                reply2 = await client.wait_for("message", timeout=60.0, check=check)
                                
                            except asyncio.TimeoutError:
                                    await reply1.channel.send(to1)
                                    session.remove(reply1.author)
#Submission Line 2 (Class Number)
                            else:
                                reply2valid = ["whittle", "vangoor", "castillo", "vecziedins", "thane", "donohue", "vogl", "beckwith", "burke", "rizley", "stachura", "jeroudi", "miller", "art", "spanish", "bio", "english", "chem", "chinese", "ess", "music", "tok", "epic", "psych"]
                                if reply2.content.lower() == "1" or reply2.content.lower() == "2" or reply2.content.lower() == "3" or reply2.content.lower() == "4" or reply2.content.lower() == "5" or reply2.content.lower() == "6" or reply2.content.lower() == "7" or reply2.content.lower() == "8" or reply2.content.lower() == "9" or reply2.content.lower() == "10" or reply2.content.lower() == "11" or reply2.content.lower() == "12" or reply2.content.lower() == "13" or reply2.content.lower() == "14" or reply2.content.lower() == "15" or reply2.content.lower() in reply2valid:
                                    if reply2.content.lower() == "1" or "whittle" in reply2.content.lower() or "art" in reply2.content.lower():
                                        classnumber = "1 - DP Visual Arts (Whittle)"
                                        classmention = "<@&806263521092173825>"
                                    elif reply2.content.lower() == "2" or "vangoor" in reply2.content.lower():
                                        classnumber = "2 - DP History (VanGoor)"
                                        classmention = "<@&806264044720750603>"
                                    elif reply2.content.lower() == "3" or "castillo" in reply2.content.lower() or "spanish" in reply2.content.lower():
                                        classnumber = "3 - Spanish (Castillo)"
                                        classmention = "<@&806264156554264607>"
                                    elif reply2.content.lower() == "4" or "vecziedins" in reply2.content.lower():
                                        classnumber = "4 - AA DP Mathematics (Vecziedins)"
                                        classmention = "<@&806264207670116405"
                                    elif reply2.content.lower() == "5" or "thane" in reply2.content.lower() or "bio" in reply2.content.lower():
                                        classnumber = "5 - DP Biology (Thane)"
                                        classmention = "<@&806264253661053010>"
                                    elif reply2.content.lower() == "6" or "donohue" in reply2.content.lower() or "english" in reply2.content.lower():
                                        classnumber = "6 - DP English (Donohue)"
                                        classmention = "<@&806264294848331835>"
                                    elif reply2.content.lower() == "7" or "vogl" in reply2.content.lower() or "chem" in reply2.content.lower():
                                        classnumber = "7 - DP Chemistry (Vogl)"
                                        classmention = "<@&806264347332575244>"
                                    elif reply2.content.lower() == "8" or "beckwith" in reply2.content.lower() or "chinese" in reply2.content.lower():
                                        classnumber = "8 - Chinese V (Beckwith)"
                                        classmention = "<@&806264428952944651>"
                                    elif reply2.content.lower() == "9" or "burke" in reply2.content.lower():
                                        classnumber = "9 - AI DP Mathematics (Burke)"
                                        classmention = "<@&806264481411366922>"
                                    elif reply2.content.lower() == "10" or "rizley" in reply2.content.lower() or "ess" in reply2.content.lower():
                                        classnumber = "10 - DP ESS (Rizley)"
                                        classmention = "<@&806264564000882748>"
                                    elif reply2.content.lower() == "11" or "stachura" in reply2.content.lower():
                                        classnumber = "11 - DP History (Stachura)"
                                        classmention = "<@&806264611392192542>"
                                    elif reply2.content.lower() == "12" or "jeroudi" in reply2.content.lower() or "music" in reply2.content.lower():
                                        classnumber = "12 - Music Theory (Jeroudi)"
                                        classmention = "<@&806264681182396467>"
                                    elif reply2.content.lower() == "13" or "tok" in reply2.content.lower():
                                        classnumber = "13 - TOK (Global)"
                                        classmention = "<@&811758649651101706>"
                                    elif reply2.content.lower() == "14" or "epic" in reply2.content.lower():
                                        classnumber = "14 - EPIC (Global)"
                                        classmention = "<@&811758892345720842>"
                                    elif reply2.content.lower() == "15" or "miller" in reply2.content.lower() or "psych" in reply2.content.lower():
                                        classnumber = "15 - Psychology (Miller)"
                                        classmention = "<@&811758978102853673>"
                                    else:
                                        classnumber = f"Null Class - Author: {reply2.author}"
                                    randr3sp1 = random.choice(r3sp1rand)
                                    randr3sp2 = random.choice(r3sp2rand)
                                    await reply2.author.send(f"{randr3sp1}`{classnumber}`.  {randr3sp2}")
                                    
                                    def check(m):
                                        return client.user.id != m.author.id and m.guild is None and m.author == reply2.author
                                    
                                    try:
                                        reply3 = await client.wait_for("message", timeout=60.0, check=check)
                                        
                                    except asyncio.TimeoutError:
                                        await reply2.channel.send(to1)
                                        session.remove(reply2.author)
#Submission Line 3 (Include Tag)
                                    else:
                                        r4srand = random.choice(r4soptions)
                                        await reply3.author.send(r4srand)
                                        
                                        def check(m):
                                            return client.user.id != m.author.id and m.guild is None and m.author == reply3.author

                                        try:
                                            reply4 = await client.wait_for("message", timeout=60.0, check=check)

                                        except asyncio.TimeoutError:
                                            await reply3.channel.send(to1)
                                            session.remove(reply3.author)
#Submission Line 4 (Note)
                                        else:
                                            r5srand = random.choice(r5soptions)
                                            await reply4.author.send(r5srand)
                                            
                                            def check(m):
                                                return client.user.id != m.author.id and m.guild is None and m.author == reply4.author
                                            
                                            try:
                                                reply5 = await client.wait_for("message", timeout=60.0, check=check)
                                                
                                            except asyncio.TimeoutError:
                                                await reply4.channel.send(to1)
                                                session.remove(reply4.author)
#Attachments
                                            else:
                                                await reply5.author.send(r6s)

                                                def check(m):
                                                    return client.user.id != m.author.id and m.guild is None and m.author == reply5.author
                                                
                                                try:
                                                    reply6 = await client.wait_for("message", timeout=60.0, check=check)
                                                    
                                                except asyncio.TimeoutError:
                                                    await reply5.channel.send(to1)
                                                    session.remove(reply5.author)
#Attachment 1
                                                else:
                                                    for attachment in reply6.attachments:
                                                        submitattach.append(attachment.url)
                                                    def check(m):
                                                        return client.user.id != m.author.id and m.guild is None and m.author == reply6.author
                                                    
                                                    try:
                                                        reply7 = await client.wait_for("message", timeout=60.0, check=check)
                                                        
                                                    except asyncio.TimeoutError:
                                                        await reply6.channel.send(to1)
                                                        session.remove(reply6.author)
                                                    else:
                                            #Query End w. 1 Attachment
                                                        if "done" in reply7.content.lower():
                                                            finalattachments = "\n".join(submitattach)
                                                #If Yes Tag
                                                            if "ye" in reply4.content.lower() or "sure" in reply4.content.lower():
                                                    #If No Note
                                                                if reply5.content.lower() == "no":
                                                                    attachcount = len(submitattach)
                                                                    embedcolor = random.choice(embedcoloroptions)
                                                                    postembed=discord.Embed(title=f"New Submission to Ironic", description=f"To {classnumber}", color=embedcolor)
                                                                    postembed.set_author(name=f"Posting as {reply7.author.name}", icon_url=f"{reply7.author.avatar_url}")
                                                                    postembed.add_field(name="Assignment Name", value=f"{reply3.content}", inline=False)
                                                                    postembed.add_field(name="Note", value="Not Included", inline=True)
                                                                    postembed.add_field(name="Tag", value="Included", inline=True)
                                                                    postembed.add_field(name="Attachment Count", value=f"{attachcount} File(s)", inline=True)
                                                                    postembed.set_footer(text="If everything looks correct, say yes.  Otherwise, say no to start over at the beginning.")
                                                                    send8 = await reply7.channel.send(r8s, embed=postembed)
                                                                    
                                                                    def check(m):
                                                                        return client.user.id != m.author.id and m.guild is None and m.author == reply7.author
                                                                    
                                                                    try:
                                                                        reply8 = await client.wait_for("message", timeout=60.0, check=check)
                                                                        
                                                                    except asyncio.TimeoutError:
                                                                        await reply6.channel.send(to1)
                                                                        session.remove(reply6.author)
                                                                    else:
                                                                        if "ye" in reply8.content.lower() or "sure" in reply8.content.lower():
                                                                            submissionforward = f"**ASSIGNMENT SUBMISSION from {reply7.author}** <@&806274913904230410> \n\n\*\*:pencil: Assignment Title:\*\* \`{reply3.content}\` \n\*\*:books: Class:\*\* \`{classnumber}\`{classmention}\n\*\*:woman_student: User:\*\* @{reply7.author} \n \n{finalattachments}"
                                                                            await reply8.channel.send(r7s)
                                                                            await botforwards.send(submissionforward)
                                                                            submitattach.clear
                                                                            session.remove(reply7.author)
                                                                        else:
                                                                            session.remove(reply7.author)
                                                    #If Yes Note
                                                                else:
                                                                    attachcount = len(submitattach)
                                                                    embedcolor = random.choice(embedcoloroptions)
                                                                    postembed=discord.Embed(title=f"New Submission to Ironic", description=f"To {classnumber}", color=embedcolor)
                                                                    postembed.set_author(name=f"Posting as {reply7.author.name}", icon_url=f"{reply7.author.avatar_url}")
                                                                    postembed.add_field(name="Assignment Name", value=f"{reply3.content}", inline=False)
                                                                    postembed.add_field(name="Note", value=f"{reply5.content}", inline=True)
                                                                    postembed.add_field(name="Tag", value="Included", inline=True)
                                                                    postembed.add_field(name="Attachment Count", value=f"{attachcount} File(s)", inline=True)
                                                                    postembed.set_footer(text="If everything looks correct, say yes.  Otherwise, say no to start over at the beginning.")
                                                                    send8 = await reply7.channel.send(r8s, embed=postembed)
                                                                    
                                                                    def check(m):
                                                                        return client.user.id != m.author.id and m.guild is None and m.author == reply7.author
                                                                    
                                                                    try:
                                                                        reply8 = await client.wait_for("message", timeout=60.0, check=check)
                                                                        
                                                                    except asyncio.TimeoutError:
                                                                        await reply6.channel.send(to1)
                                                                        session.remove(reply6.author)
                                                                    else:
                                                                        if "ye" in reply8.content.lower() or "sure" in reply8.content.lower():
                                                                            submissionforward = f"**ASSIGNMENT SUBMISSION from {reply7.author}** <@&806274913904230410> \n\n\*\*:pencil: Assignment Title:\*\* \`{reply3.content}\` \n\*\*:books: Class:\*\* \`{classnumber}\`{classmention}\n\*\*:woman_student: User:\*\* @{reply7.author}\n \n\*\*:notepad_spiral: Submission Notes:\*\* \`{reply5.content}\` \n \n{finalattachments}"
                                                                            await reply8.channel.send(r7s)
                                                                            await botforwards.send(submissionforward)
                                                                            submitattach.clear
                                                                            session.remove(reply7.author)
                                                                        else:
                                                                            session.remove(reply7.author)
                                                #If No Tag
                                                            else:
                                                                if reply5.content.lower() == "no":
                                                    #If No Note
                                                                    attachcount = len(submitattach)
                                                                    embedcolor = random.choice(embedcoloroptions)
                                                                    postembed=discord.Embed(title=f"New Submission to Ironic", description=f"To {classnumber}", color=embedcolor)
                                                                    postembed.set_author(name=f"Posting as Anonymous", icon_url=f"{client.user.avatar_url}")
                                                                    postembed.add_field(name="Assignment Name", value=f"{reply3.content}", inline=False)
                                                                    postembed.add_field(name="Note", value="Not Included", inline=True)
                                                                    postembed.add_field(name="Tag", value="Included", inline=True)
                                                                    postembed.add_field(name="Attachment Count", value=f"{attachcount} File(s)", inline=True)
                                                                    postembed.set_footer(text="If everything looks correct, say yes.  Otherwise, say no to start over at the beginning.")
                                                                    send8 = await reply7.channel.send(r8s, embed=postembed)
                                                                    
                                                                    def check(m):
                                                                        return client.user.id != m.author.id and m.guild is None and m.author == reply7.author
                                                                    
                                                                    try:
                                                                        reply8 = await client.wait_for("message", timeout=60.0, check=check)
                                                                        
                                                                    except asyncio.TimeoutError:
                                                                        await reply6.channel.send(to1)
                                                                        session.remove(reply6.author)
                                                                    else:
                                                                        if "ye" in reply8.content.lower() or "sure" in reply8.content.lower():
                                                                            submissionforward = f"**ASSIGNMENT SUBMISSION** <@&806274913904230410> \n\n\*\*:pencil: Assignment Title:\*\* \`{reply3.content}\` \n\*\*:books: Class:\*\* \`{classnumber}\`{classmention}\n \n{finalattachments}"
                                                                            await reply8.channel.send(r7s)
                                                                            await botforwards.send(submissionforward)
                                                                            submitattach.clear
                                                                            session.remove(reply7.author)
                                                                        else:
                                                                            session.remove(reply7.author)
                                                    #If Yes Note
                                                                else:
                                                                    attachcount = len(submitattach)
                                                                    embedcolor = random.choice(embedcoloroptions)
                                                                    postembed=discord.Embed(title=f"New Submission to Ironic", description=f"To {classnumber}", color=embedcolor)
                                                                    postembed.set_author(name=f"Posting as Anonymous", icon_url=f"{client.user.avatar_url}")
                                                                    postembed.add_field(name="Assignment Name", value=f"{reply3.content}", inline=False)
                                                                    postembed.add_field(name="Note", value=f"{reply5.content}", inline=True)
                                                                    postembed.add_field(name="Tag", value="Included", inline=True)
                                                                    postembed.add_field(name="Attachment Count", value=f"{attachcount} File(s)", inline=True)
                                                                    postembed.set_footer(text="If everything looks correct, say yes.  Otherwise, say no to start over at the beginning.")
                                                                    send8 = await reply7.channel.send(r8s, embed=postembed)
                                                                    
                                                                    def check(m):
                                                                        return client.user.id != m.author.id and m.guild is None and m.author == reply7.author
                                                                    
                                                                    try:
                                                                        reply8 = await client.wait_for("message", timeout=60.0, check=check)
                                                                        
                                                                    except asyncio.TimeoutError:
                                                                        await reply6.channel.send(to1)
                                                                        session.remove(reply6.author)
                                                                    else:
                                                                        if "ye" in reply8.content.lower() or "sure" in reply8.content.lower():
                                                                            submissionforward = f"**ASSIGNMENT SUBMISSION** <@&806274913904230410> \n\n\*\*:pencil: Assignment Title:\*\* \`{reply3.content}\` \n\*\*:books: Class:\*\* \`{classnumber}\`{classmention}\n \n\*\*:notepad_spiral: Submission Notes:\*\* \`{reply5.content}\` \n \n{finalattachments}"
                                                                            await reply8.channel.send(r7s)
                                                                            await botforwards.send(submissionforward)
                                                                            submitattach.clear
                                                                            session.remove(reply7.author)
                                                                        else:
                                                                            session.remove(reply7.author)
#Attachment 2
                                                        else:
                                                            for attachment in reply7.attachments:
                                                                submitattach.append(attachment.url)
                                                            def check(m):
                                                                return client.user.id != m.author.id and m.guild is None and m.author == reply7.author
                                                            
                                                            try:
                                                                reply8 = await client.wait_for("message", timeout=60.0, check=check)
                                                                
                                                            except asyncio.TimeoutError:
                                                                await reply7.channel.send(to1)
                                                                session.remove(reply7.author)
                                                            else:
                                                                if "done" in reply8.content.lower():
                                                                    finalattachments = "\n".join(submitattach)
                                                        #If Yes Tag
                                                                    if "ye" in reply4.content.lower() or "sure" in reply4.content.lower():
                                                            #If No Note
                                                                        if reply5.content.lower() == "no":
                                                                            attachcount = len(submitattach)
                                                                            embedcolor = random.choice(embedcoloroptions)
                                                                            postembed=discord.Embed(title=f"New Submission to Ironic", description=f"To {classnumber}", color=embedcolor)
                                                                            postembed.set_author(name=f"Posting as {reply7.author.name}", icon_url=f"{reply7.author.avatar_url}")
                                                                            postembed.add_field(name="Assignment Name", value=f"{reply3.content}", inline=False)
                                                                            postembed.add_field(name="Note", value="Not Included", inline=True)
                                                                            postembed.add_field(name="Tag", value="Included", inline=True)
                                                                            postembed.add_field(name="Attachment Count", value=f"{attachcount} File(s)", inline=True)
                                                                            postembed.set_footer(text="If everything looks correct, say yes.  Otherwise, say no to start over at the beginning.")
                                                                            send8 = await reply7.channel.send(r8s, embed=postembed)
                                                                            
                                                                            def check(m):
                                                                                return client.user.id != m.author.id and m.guild is None and m.author == reply7.author
                                                                            
                                                                            try:
                                                                                reply8 = await client.wait_for("message", timeout=60.0, check=check)
                                                                                
                                                                            except asyncio.TimeoutError:
                                                                                await reply6.channel.send(to1)
                                                                                session.remove(reply6.author)
                                                                            else:
                                                                                if "ye" in reply8.content.lower() or "sure" in reply8.content.lower():
                                                                                    submissionforward = f"**ASSIGNMENT SUBMISSION from {reply7.author}** <@&806274913904230410> \n\n\*\*:pencil: Assignment Title:\*\* \`{reply3.content}\` \n\*\*:books: Class:\*\* \`{classnumber}\`{classmention}\n\*\*:woman_student: User:\*\* @{reply7.author} \n \n{finalattachments}"
                                                                                    await reply8.channel.send(r7s)
                                                                                    await botforwards.send(submissionforward)
                                                                                    submitattach.clear
                                                                                    session.remove(reply7.author)
                                                                                else:
                                                                                    session.remove(reply7.author)
                                                            #If Yes Note
                                                                        else:
                                                                            attachcount = len(submitattach)
                                                                            embedcolor = random.choice(embedcoloroptions)
                                                                            postembed=discord.Embed(title=f"New Submission to Ironic", description=f"To {classnumber}", color=embedcolor)
                                                                            postembed.set_author(name=f"Posting as {reply7.author.name}", icon_url=f"{reply7.author.avatar_url}")
                                                                            postembed.add_field(name="Assignment Name", value=f"{reply3.content}", inline=False)
                                                                            postembed.add_field(name="Note", value=f"{reply5.content}", inline=True)
                                                                            postembed.add_field(name="Tag", value="Included", inline=True)
                                                                            postembed.add_field(name="Attachment Count", value=f"{attachcount} File(s)", inline=True)
                                                                            postembed.set_footer(text="If everything looks correct, say yes.  Otherwise, say no to start over at the beginning.")
                                                                            send8 = await reply7.channel.send(r8s, embed=postembed)
                                                                            
                                                                            def check(m):
                                                                                return client.user.id != m.author.id and m.guild is None and m.author == reply7.author
                                                                            
                                                                            try:
                                                                                reply8 = await client.wait_for("message", timeout=60.0, check=check)
                                                                                
                                                                            except asyncio.TimeoutError:
                                                                                await reply6.channel.send(to1)
                                                                                session.remove(reply6.author)
                                                                            else:
                                                                                if "ye" in reply8.content.lower() or "sure" in reply8.content.lower():
                                                                                    submissionforward = f"**ASSIGNMENT SUBMISSION from {reply7.author}** <@&806274913904230410> \n\n\*\*:pencil: Assignment Title:\*\* \`{reply3.content}\` \n\*\*:books: Class:\*\* \`{classnumber}\`{classmention}\n\*\*:woman_student: User:\*\* @{reply7.author}\n \n\*\*:notepad_spiral: Submission Notes:\*\* \`{reply5.content}\` \n \n{finalattachments}"
                                                                                    await reply8.channel.send(r7s)
                                                                                    await botforwards.send(submissionforward)
                                                                                    submitattach.clear
                                                                                    session.remove(reply7.author)
                                                                                else:
                                                                                    session.remove(reply7.author)
                                                        #If No Tag
                                                                    else:
                                                                        if reply5.content.lower() == "no":
                                                            #If No Note
                                                                            attachcount = len(submitattach)
                                                                            embedcolor = random.choice(embedcoloroptions)
                                                                            postembed=discord.Embed(title=f"New Submission to Ironic", description=f"To {classnumber}", color=embedcolor)
                                                                            postembed.set_author(name=f"Posting as Anonymous", icon_url=f"{client.user.avatar_url}")
                                                                            postembed.add_field(name="Assignment Name", value=f"{reply3.content}", inline=False)
                                                                            postembed.add_field(name="Note", value="Not Included", inline=True)
                                                                            postembed.add_field(name="Tag", value="Included", inline=True)
                                                                            postembed.add_field(name="Attachment Count", value=f"{attachcount} File(s)", inline=True)
                                                                            postembed.set_footer(text="If everything looks correct, say yes.  Otherwise, say no to start over at the beginning.")
                                                                            send8 = await reply7.channel.send(r8s, embed=postembed)
                                                                            
                                                                            def check(m):
                                                                                return client.user.id != m.author.id and m.guild is None and m.author == reply7.author
                                                                            
                                                                            try:
                                                                                reply8 = await client.wait_for("message", timeout=60.0, check=check)
                                                                                
                                                                            except asyncio.TimeoutError:
                                                                                await reply6.channel.send(to1)
                                                                                session.remove(reply6.author)
                                                                            else:
                                                                                if "ye" in reply8.content.lower() or "sure" in reply8.content.lower():
                                                                                    submissionforward = f"**ASSIGNMENT SUBMISSION** <@&806274913904230410> \n\n\*\*:pencil: Assignment Title:\*\* \`{reply3.content}\` \n\*\*:books: Class:\*\* \`{classnumber}\`{classmention}\n \n{finalattachments}"
                                                                                    await reply8.channel.send(r7s)
                                                                                    await botforwards.send(submissionforward)
                                                                                    submitattach.clear
                                                                                    session.remove(reply7.author)
                                                                                else:
                                                                                    session.remove(reply7.author)
                                                            #If Yes Note
                                                                        else:
                                                                            attachcount = len(submitattach)
                                                                            embedcolor = random.choice(embedcoloroptions)
                                                                            postembed=discord.Embed(title=f"New Submission to Ironic", description=f"To {classnumber}", color=embedcolor)
                                                                            postembed.set_author(name=f"Posting as Anonymous", icon_url=f"{client.user.avatar_url}")
                                                                            postembed.add_field(name="Assignment Name", value=f"{reply3.content}", inline=False)
                                                                            postembed.add_field(name="Note", value=f"{reply5.content}", inline=True)
                                                                            postembed.add_field(name="Tag", value="Included", inline=True)
                                                                            postembed.add_field(name="Attachment Count", value=f"{attachcount} File(s)", inline=True)
                                                                            postembed.set_footer(text="If everything looks correct, say yes.  Otherwise, say no to start over at the beginning.")
                                                                            send8 = await reply7.channel.send(r8s, embed=postembed)
                                                                            
                                                                            def check(m):
                                                                                return client.user.id != m.author.id and m.guild is None and m.author == reply7.author
                                                                            
                                                                            try:
                                                                                reply8 = await client.wait_for("message", timeout=60.0, check=check)
                                                                                
                                                                            except asyncio.TimeoutError:
                                                                                await reply6.channel.send(to1)
                                                                                session.remove(reply6.author)
                                                                            else:
                                                                                if "ye" in reply8.content.lower() or "sure" in reply8.content.lower():
                                                                                    submissionforward = f"**ASSIGNMENT SUBMISSION** <@&806274913904230410> \n\n\*\*:pencil: Assignment Title:\*\* \`{reply3.content}\` \n\*\*:books: Class:\*\* \`{classnumber}\`{classmention}\n \n\*\*:notepad_spiral: Submission Notes:\*\* \`{reply5.content}\` \n \n{finalattachments}"
                                                                                    await reply8.channel.send(r7s)
                                                                                    await botforwards.send(submissionforward)
                                                                                    submitattach.clear
                                                                                    session.remove(reply7.author)
                                                                                else:
                                                                                    session.remove(reply7.author)
#Attachment 4
                                                                else:
                                                                    if "done" in reply9.content.lower():
                                                                        finalattachments = "\n".join(submitattach)
                                                            #If Yes Tag
                                                                        if "ye" in reply4.content.lower() or "sure" in reply4.content.lower():
                                                                #If No Note
                                                                            if reply5.content.lower() == "no":
                                                                                attachcount = len(submitattach)
                                                                                embedcolor = random.choice(embedcoloroptions)
                                                                                postembed=discord.Embed(title=f"New Submission to Ironic", description=f"To {classnumber}", color=embedcolor)
                                                                                postembed.set_author(name=f"Posting as {reply7.author.name}", icon_url=f"{reply7.author.avatar_url}")
                                                                                postembed.add_field(name="Assignment Name", value=f"{reply3.content}", inline=False)
                                                                                postembed.add_field(name="Note", value="Not Included", inline=True)
                                                                                postembed.add_field(name="Tag", value="Included", inline=True)
                                                                                postembed.add_field(name="Attachment Count", value=f"{attachcount} File(s)", inline=True)
                                                                                postembed.set_footer(text="If everything looks correct, say yes.  Otherwise, say no to start over at the beginning.")
                                                                                send8 = await reply7.channel.send(r8s, embed=postembed)
                                                                                
                                                                                def check(m):
                                                                                    return client.user.id != m.author.id and m.guild is None and m.author == reply7.author
                                                                                
                                                                                try:
                                                                                    reply8 = await client.wait_for("message", timeout=60.0, check=check)
                                                                                    
                                                                                except asyncio.TimeoutError:
                                                                                    await reply6.channel.send(to1)
                                                                                    session.remove(reply6.author)
                                                                                else:
                                                                                    if "ye" in reply8.content.lower() or "sure" in reply8.content.lower():
                                                                                        submissionforward = f"**ASSIGNMENT SUBMISSION from {reply7.author}** <@&806274913904230410> \n\n\*\*:pencil: Assignment Title:\*\* \`{reply3.content}\` \n\*\*:books: Class:\*\* \`{classnumber}\`{classmention}\n\*\*:woman_student: User:\*\* @{reply7.author} \n \n{finalattachments}"
                                                                                        await reply8.channel.send(r7s)
                                                                                        await botforwards.send(submissionforward)
                                                                                        submitattach.clear
                                                                                        session.remove(reply7.author)
                                                                                    else:
                                                                                        session.remove(reply7.author)
                                                                #If Yes Note
                                                                            else:
                                                                                attachcount = len(submitattach)
                                                                                embedcolor = random.choice(embedcoloroptions)
                                                                                postembed=discord.Embed(title=f"New Submission to Ironic", description=f"To {classnumber}", color=embedcolor)
                                                                                postembed.set_author(name=f"Posting as {reply7.author.name}", icon_url=f"{reply7.author.avatar_url}")
                                                                                postembed.add_field(name="Assignment Name", value=f"{reply3.content}", inline=False)
                                                                                postembed.add_field(name="Note", value=f"{reply5.content}", inline=True)
                                                                                postembed.add_field(name="Tag", value="Included", inline=True)
                                                                                postembed.add_field(name="Attachment Count", value=f"{attachcount} File(s)", inline=True)
                                                                                postembed.set_footer(text="If everything looks correct, say yes.  Otherwise, say no to start over at the beginning.")
                                                                                send8 = await reply7.channel.send(r8s, embed=postembed)
                                                                                
                                                                                def check(m):
                                                                                    return client.user.id != m.author.id and m.guild is None and m.author == reply7.author
                                                                                
                                                                                try:
                                                                                    reply8 = await client.wait_for("message", timeout=60.0, check=check)
                                                                                    
                                                                                except asyncio.TimeoutError:
                                                                                    await reply6.channel.send(to1)
                                                                                    session.remove(reply6.author)
                                                                                else:
                                                                                    if "ye" in reply8.content.lower() or "sure" in reply8.content.lower():
                                                                                        submissionforward = f"**ASSIGNMENT SUBMISSION from {reply7.author}** <@&806274913904230410> \n\n\*\*:pencil: Assignment Title:\*\* \`{reply3.content}\` \n\*\*:books: Class:\*\* \`{classnumber}\`{classmention}\n\*\*:woman_student: User:\*\* @{reply7.author}\n \n\*\*:notepad_spiral: Submission Notes:\*\* \`{reply5.content}\` \n \n{finalattachments}"
                                                                                        await reply8.channel.send(r7s)
                                                                                        await botforwards.send(submissionforward)
                                                                                        submitattach.clear
                                                                                        session.remove(reply7.author)
                                                                                    else:
                                                                                        session.remove(reply7.author)
                                                            #If No Tag
                                                                        else:
                                                                            if reply5.content.lower() == "no":
                                                                #If No Note
                                                                                attachcount = len(submitattach)
                                                                                embedcolor = random.choice(embedcoloroptions)
                                                                                postembed=discord.Embed(title=f"New Submission to Ironic", description=f"To {classnumber}", color=embedcolor)
                                                                                postembed.set_author(name=f"Posting as Anonymous", icon_url=f"{client.user.avatar_url}")
                                                                                postembed.add_field(name="Assignment Name", value=f"{reply3.content}", inline=False)
                                                                                postembed.add_field(name="Note", value="Not Included", inline=True)
                                                                                postembed.add_field(name="Tag", value="Included", inline=True)
                                                                                postembed.add_field(name="Attachment Count", value=f"{attachcount} File(s)", inline=True)
                                                                                postembed.set_footer(text="If everything looks correct, say yes.  Otherwise, say no to start over at the beginning.")
                                                                                send8 = await reply7.channel.send(r8s, embed=postembed)
                                                                                
                                                                                def check(m):
                                                                                    return client.user.id != m.author.id and m.guild is None and m.author == reply7.author
                                                                                
                                                                                try:
                                                                                    reply8 = await client.wait_for("message", timeout=60.0, check=check)
                                                                                    
                                                                                except asyncio.TimeoutError:
                                                                                    await reply6.channel.send(to1)
                                                                                    session.remove(reply6.author)
                                                                                else:
                                                                                    if "ye" in reply8.content.lower() or "sure" in reply8.content.lower():
                                                                                        submissionforward = f"**ASSIGNMENT SUBMISSION** <@&806274913904230410> \n\n\*\*:pencil: Assignment Title:\*\* \`{reply3.content}\` \n\*\*:books: Class:\*\* \`{classnumber}\`{classmention}\n \n{finalattachments}"
                                                                                        await reply8.channel.send(r7s)
                                                                                        await botforwards.send(submissionforward)
                                                                                        submitattach.clear
                                                                                        session.remove(reply7.author)
                                                                                    else:
                                                                                        session.remove(reply7.author)
                                                                #If Yes Note
                                                                            else:
                                                                                attachcount = len(submitattach)
                                                                                embedcolor = random.choice(embedcoloroptions)
                                                                                postembed=discord.Embed(title=f"New Submission to Ironic", description=f"To {classnumber}", color=embedcolor)
                                                                                postembed.set_author(name=f"Posting as Anonymous", icon_url=f"{client.user.avatar_url}")
                                                                                postembed.add_field(name="Assignment Name", value=f"{reply3.content}", inline=False)
                                                                                postembed.add_field(name="Note", value=f"{reply5.content}", inline=True)
                                                                                postembed.add_field(name="Tag", value="Included", inline=True)
                                                                                postembed.add_field(name="Attachment Count", value=f"{attachcount} File(s)", inline=True)
                                                                                postembed.set_footer(text="If everything looks correct, say yes.  Otherwise, say no to start over at the beginning.")
                                                                                send8 = await reply7.channel.send(r8s, embed=postembed)
                                                                                
                                                                                def check(m):
                                                                                    return client.user.id != m.author.id and m.guild is None and m.author == reply7.author
                                                                                
                                                                                try:
                                                                                    reply8 = await client.wait_for("message", timeout=60.0, check=check)
                                                                                    
                                                                                except asyncio.TimeoutError:
                                                                                    await reply6.channel.send(to1)
                                                                                    session.remove(reply6.author)
                                                                                else:
                                                                                    if "ye" in reply8.content.lower() or "sure" in reply8.content.lower():
                                                                                        submissionforward = f"**ASSIGNMENT SUBMISSION** <@&806274913904230410> \n\n\*\*:pencil: Assignment Title:\*\* \`{reply3.content}\` \n\*\*:books: Class:\*\* \`{classnumber}\`{classmention}\n \n\*\*:notepad_spiral: Submission Notes:\*\* \`{reply5.content}\` \n \n{finalattachments}"
                                                                                        await reply8.channel.send(r7s)
                                                                                        await botforwards.send(submissionforward)
                                                                                        submitattach.clear
                                                                                        session.remove(reply7.author)
                                                                                    else:
                                                                                        session.remove(reply7.author)
#Attachment 5
                                                                    else:
                                                                        if "done" in reply10.content.lower():
                                                                            finalattachments = "\n".join(submitattach)
                                                                #If Yes Tag
                                                                            if "ye" in reply4.content.lower() or "sure" in reply4.content.lower():
                                                                    #If No Note
                                                                                if reply5.content.lower() == "no":
                                                                                    attachcount = len(submitattach)
                                                                                    embedcolor = random.choice(embedcoloroptions)
                                                                                    postembed=discord.Embed(title=f"New Submission to Ironic", description=f"To {classnumber}", color=embedcolor)
                                                                                    postembed.set_author(name=f"Posting as {reply7.author.name}", icon_url=f"{reply7.author.avatar_url}")
                                                                                    postembed.add_field(name="Assignment Name", value=f"{reply3.content}", inline=False)
                                                                                    postembed.add_field(name="Note", value="Not Included", inline=True)
                                                                                    postembed.add_field(name="Tag", value="Included", inline=True)
                                                                                    postembed.add_field(name="Attachment Count", value=f"{attachcount} File(s)", inline=True)
                                                                                    postembed.set_footer(text="If everything looks correct, say yes.  Otherwise, say no to start over at the beginning.")
                                                                                    send8 = await reply7.channel.send(r8s, embed=postembed)
                                                                                    
                                                                                    def check(m):
                                                                                        return client.user.id != m.author.id and m.guild is None and m.author == reply7.author
                                                                                    
                                                                                    try:
                                                                                        reply8 = await client.wait_for("message", timeout=60.0, check=check)
                                                                                        
                                                                                    except asyncio.TimeoutError:
                                                                                        await reply6.channel.send(to1)
                                                                                        session.remove(reply6.author)
                                                                                    else:
                                                                                        if "ye" in reply8.content.lower() or "sure" in reply8.content.lower():
                                                                                            submissionforward = f"**ASSIGNMENT SUBMISSION from {reply7.author}** <@&806274913904230410> \n\n\*\*:pencil: Assignment Title:\*\* \`{reply3.content}\` \n\*\*:books: Class:\*\* \`{classnumber}\`{classmention}\n\*\*:woman_student: User:\*\* @{reply7.author} \n \n{finalattachments}"
                                                                                            await reply8.channel.send(r7s)
                                                                                            await botforwards.send(submissionforward)
                                                                                            submitattach.clear
                                                                                            session.remove(reply7.author)
                                                                                        else:
                                                                                            session.remove(reply7.author)
                                                                    #If Yes Note
                                                                                else:
                                                                                    attachcount = len(submitattach)
                                                                                    embedcolor = random.choice(embedcoloroptions)
                                                                                    postembed=discord.Embed(title=f"New Submission to Ironic", description=f"To {classnumber}", color=embedcolor)
                                                                                    postembed.set_author(name=f"Posting as {reply7.author.name}", icon_url=f"{reply7.author.avatar_url}")
                                                                                    postembed.add_field(name="Assignment Name", value=f"{reply3.content}", inline=False)
                                                                                    postembed.add_field(name="Note", value=f"{reply5.content}", inline=True)
                                                                                    postembed.add_field(name="Tag", value="Included", inline=True)
                                                                                    postembed.add_field(name="Attachment Count", value=f"{attachcount} File(s)", inline=True)
                                                                                    postembed.set_footer(text="If everything looks correct, say yes.  Otherwise, say no to start over at the beginning.")
                                                                                    send8 = await reply7.channel.send(r8s, embed=postembed)
                                                                                    
                                                                                    def check(m):
                                                                                        return client.user.id != m.author.id and m.guild is None and m.author == reply7.author

                                                                                    try:
                                                                                        reply8 = await client.wait_for("message", timeout=60.0, check=check)

                                                                                    except asyncio.TimeoutError:
                                                                                        await reply6.channel.send(to1)
                                                                                        session.remove(reply6.author)
                                                                                    else:
                                                                                        if "ye" in reply8.content.lower() or "sure" in reply8.content.lower():
                                                                                            submissionforward = f"**ASSIGNMENT SUBMISSION from {reply7.author}** <@&806274913904230410> \n\n\*\*:pencil: Assignment Title:\*\* \`{reply3.content}\` \n\*\*:books: Class:\*\* \`{classnumber}\`{classmention}\n\*\*:woman_student: User:\*\* @{reply7.author}\n \n\*\*:notepad_spiral: Submission Notes:\*\* \`{reply5.content}\` \n \n{finalattachments}"
                                                                                            await reply8.channel.send(r7s)
                                                                                            await botforwards.send(submissionforward)
                                                                                            submitattach.clear
                                                                                            session.remove(reply7.author)
                                                                                        else:
                                                                                            session.remove(reply7.author)
                                                                #If No Tag
                                                                            else:
                                                                                if reply5.content.lower() == "no":
                                                                    #If No Note
                                                                                    attachcount = len(submitattach)
                                                                                    embedcolor = random.choice(embedcoloroptions)
                                                                                    postembed=discord.Embed(title=f"New Submission to Ironic", description=f"To {classnumber}", color=embedcolor)
                                                                                    postembed.set_author(name=f"Posting as Anonymous", icon_url=f"{client.user.avatar_url}")
                                                                                    postembed.add_field(name="Assignment Name", value=f"{reply3.content}", inline=False)
                                                                                    postembed.add_field(name="Note", value="Not Included", inline=True)
                                                                                    postembed.add_field(name="Tag", value="Included", inline=True)
                                                                                    postembed.add_field(name="Attachment Count", value=f"{attachcount} File(s)", inline=True)
                                                                                    postembed.set_footer(text="If everything looks correct, say yes.  Otherwise, say no to start over at the beginning.")
                                                                                    send8 = await reply7.channel.send(r8s, embed=postembed)
                                                                                    
                                                                                    def check(m):
                                                                                        return client.user.id != m.author.id and m.guild is None and m.author == reply7.author
                                                                                    
                                                                                    try:
                                                                                        reply8 = await client.wait_for("message", timeout=60.0, check=check)
                                                                                        
                                                                                    except asyncio.TimeoutError:
                                                                                        await reply6.channel.send(to1)
                                                                                        session.remove(reply6.author)
                                                                                    else:
                                                                                        if "ye" in reply8.content.lower() or "sure" in reply8.content.lower():
                                                                                            submissionforward = f"**ASSIGNMENT SUBMISSION** <@&806274913904230410> \n\n\*\*:pencil: Assignment Title:\*\* \`{reply3.content}\` \n\*\*:books: Class:\*\* \`{classnumber}\`{classmention}\n \n{finalattachments}"
                                                                                            await reply8.channel.send(r7s)
                                                                                            await botforwards.send(submissionforward)
                                                                                            submitattach.clear
                                                                                            session.remove(reply7.author)
                                                                                        else:
                                                                                            session.remove(reply7.author)
                                                                    #If Yes Note
                                                                                else:
                                                                                    attachcount = len(submitattach)
                                                                                    embedcolor = random.choice(embedcoloroptions)
                                                                                    postembed=discord.Embed(title=f"New Submission to Ironic", description=f"To {classnumber}", color=embedcolor)
                                                                                    postembed.set_author(name=f"Posting as Anonymous", icon_url=f"{client.user.avatar_url}")
                                                                                    postembed.add_field(name="Assignment Name", value=f"{reply3.content}", inline=False)
                                                                                    postembed.add_field(name="Note", value=f"{reply5.content}", inline=True)
                                                                                    postembed.add_field(name="Tag", value="Included", inline=True)
                                                                                    postembed.add_field(name="Attachment Count", value=f"{attachcount} File(s)", inline=True)
                                                                                    postembed.set_footer(text="If everything looks correct, say yes.  Otherwise, say no to start over at the beginning.")
                                                                                    send8 = await reply7.channel.send(r8s, embed=postembed)

                                                                                    def check(m):
                                                                                        return client.user.id != m.author.id and m.guild is None and m.author == reply7.author

                                                                                    try:
                                                                                        reply8 = await client.wait_for("message", timeout=60.0, check=check)

                                                                                    except asyncio.TimeoutError:
                                                                                        await reply6.channel.send(to1)
                                                                                        session.remove(reply6.author)
                                                                                    else:
                                                                                        if "ye" in reply8.content.lower() or "sure" in reply8.content.lower():
                                                                                            submissionforward = f"**ASSIGNMENT SUBMISSION** <@&806274913904230410> \n\n\*\*:pencil: Assignment Title:\*\* \`{reply3.content}\` \n\*\*:books: Class:\*\* \`{classnumber}\`{classmention}\n \n\*\*:notepad_spiral: Submission Notes:\*\* \`{reply5.content}\` \n \n{finalattachments}"
                                                                                            await reply8.channel.send(r7s)
                                                                                            await botforwards.send(submissionforward)
                                                                                            submitattach.clear
                                                                                            session.remove(reply7.author)
                                                                                        else:
                                                                                            session.remove(reply7.author)
#Attachment Overload
                                                                        else:
                                                                            if "done" in reply11.content.lower():
                                                                                await reply10.channel.send(r7s)
                                                                                botforwards = client.get_channel(813872172799754250)
                                                                                submissionforward = f"**ASSIGNMENT SUBMISSION from {reply10.author}** <@&806274913904230410> \n\n\*\*:pencil: Assignment Title:\*\* \`{reply3.content}\` \n\*\*:books: Class:\*\* \`{classnumber}\`{classmention}\n\*\*:woman_student: User:\*\* @{reply7.author} \n \n{finalattachments}"
                                                                                await botforwards.send(submissionforward)
                                                                                submitattach.clear
                                                                                session.remove(reply11.author)
                                                                            else:
                                                                                await reply11.channel.send(ol3)
                                                                                session.remove(reply11.author)
#Errors

                            #Class Inval
                                else:
                                    randominvalclass = random.choice(invalclass)
                                    await reply2.author.send(randominvalclass)
                                    session.remove(reply2.author)

#Alt Lines
                        elif "join class" in reply1.content.lower() or "\U0001f4da" in reply1.content.lower():
                            await reply1.author.send(r2j)
                            session.remove(reply1.author)
                            
                        elif "leave class" in reply1.content.lower():
                            await reply1.author.send(r2l)
                            session.remove(reply1.author)
                            
                        elif "join/leave" in reply1.content.lower():
                            await reply1.author.send(r2jl)
                            session.remove(reply1.author)
                            
                        elif "correct" in reply1.content.lower() or "correction" in reply1.content.lower() or "\U00002705" in reply1.content.lower():
                            await reply1.author.send("This string is incomplete.  Please select another option.")
                            session.remove(reply1.author)
                            
                        elif "help" in reply1.content.lower() or "\U0001f527" in reply1.content.lower():
                            await reply1.author.send("This string is incomplete.  Please select another option.")
                            session.remove(reply1.author)
                            
                        elif "club" in reply1.content.lower():
                            await reply1.author.send(r2jl)
                            session.remove(reply1.author)
                            
                        else:
                            await reply1.author.send(e1)
                            await reply1.author.send(e2)
                            session.remove(reply1.author)
#Meme Response
            else:
                if message.channel == client.get_channel(808452909367820288):
                    if message.attachments:
                        await message.add_reaction("<:good_meme:808824921484558348>")
                        await message.add_reaction("<:bad_meme:808826207361695786>")
#Moderator Post
                elif message.channel == client.get_channel(822602852609687552):
                    if "assignment title" in message.content.lower() and "class" in message.content.lower() and "assignment id" in message.content.lower():
                        tokena = secrets.token_hex(30)
                        await message.add_reaction("<:logo:823040639058837505>")
                        await message.channel.send(":white_check_mark: Section 1 Clear", delete_after=3)
                        await message.channel.send(":white_check_mark: Section 2 Clear", delete_after=3)
                        await message.channel.send(":white_check_mark: Section 3 Clear", delete_after=3)
                        await message.channel.send(":ballot_box_with_check: Transaction has been cleared to T1.  Generating unique hash...", delete_after=5)
                        await message.author.send(f":hash: Your Post ID is `0x{tokena}`")
                        userid = message.author.id
                        await message.channel.send(f":hash: Hash ID: `0x{tokena}` <@{userid}>")
                        forwardchannel = client.get_channel(822618074548535378)
                        forward = f"`{message.author.name}` submitted a post query. \n ID: `0x{tokena}` \n```{message.content}```"
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

client.run(TOKEN)
