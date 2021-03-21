import discord
from discord.ext import commands
from discord.utils import get
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=',', intents=intents)
session = []

#Member_Join
r1 = ":wave: Welcome to the server!  I am a bot that can help to hook you up with the correct roles.  But first, in accordance with the server's privacy policy, I need to make sure that you're a good fit for the server.  Is this a good time to ask a few questions?  Your responses will not be shared or externally stored in any way after you are approved."
r2y = ":white_check_mark: Great!  Let's start with your full name and birthday.  Anonymous accounts ARE allowed within the server (for those with privacy concerns), but we do require a name upon entry to make sure that you go to City."
r2n = ":no_entry: No worries!  Simply say anything to alert the bot when you're ready."
r2f = ":wave: Heya!  I just wanted to follow up to make sure you recieved my previous message.  Before I can enter you into the server, I need to ask a few questions.  Is now a good time to do that?"

#Approval
r3a = "Got it, let me forward your info to the server owner so I can get you approved.  Once that's done, I'll we'll get your classes set up, and show you around the server.
r3al2 = "If the owner isn't online at the moment, we'll continue this entry process as soon as they come online.  Thanks for being patient!"

#Approval Errors
aerr1 = ":smiling_face_with_tear: Sorry, it seems as though you havent provided a full name or birthdate.  Please provide your full first and last name, with the appropriate birthdate included."
errordenied = "Well, this is awkward.  Sadly, it looks like the server owner has denied you for entry.  Feel free to reach out to them directly if you feel as though this is unjustified."

#Post Approval
r4 = "Great news!  The server owner has approved you for entry!  When you're ready, say anything to continue."
r4c = f":books: Welcome back!  Let's finish this setup process.  What classes are you in?  We currently support the following classes:\n1 - DP Visual Arts (Whittle)\n2 - DP History (VanGoor)\n3 - Spanish V (Castillo)\n4 - AA Mathematics (Vecziedins)\n5 - DP Biology (Thane)\n6 - DP English (Donohue)\n7 - DP Chemistry (Vogl)\n8 - Chinese V (Beckwith)\n9 - AI Mathematics (Burke)\n10 - DP ESS (Rizley)\n11 - DP History (Stachura)\n12 - Music Theory (Jeroudi)\n13 - TOK (Global)\n14 - EPIC (Global)\n15 - Psychology (Miller)\nRespond with the according class number, and remember that you can add/remove classes later!"
r5t = "Great!  One last thing; to keep this server safe, it's important that you read the TOS and Privacy Policy, which you should now be able to find within the server.  When you've finished reading those, send the phrase provided in the TOS channel.  This step is required for entry."

#Final
r5 = ":tada: Awesome, thanks for reading those!  Welcome to the server, I'll get your roles setup now.  While I'm doing that, check out this video which will help you understand the server in a bit more detail."
r6 = "You should now have the correct roles.  Please reach out to a moderator if you can't see all of the classes that you applied for. :heart: WELCOME TO THE SERVER! :heart:"

#Errors

@client.event
async def on_ready():
    print(f"{client.user.name} is online!")
    user = client.get_channel(822482846119231536)
    forward = f"`{client.user.name}` is online!"
    await user.send(forward)
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="for new members!"))

@client.event
async def on_message(message):
    if message.author.id != client.user.id:
        if message.guild is None:
            if "$s-reset" in message.content.lower():
                await message.author.send("Restarting Session")
                session.clear()
                print("Session Restarted")
            elif "$s-list" in message.content.lower():
                for sessions in session:
                    await message.author.send(sessions)
            else:
                if message.author.name not in session:
                    await message.author.send("Sorry, but this bot is still in development.  Please forward any questions or comments to a moderator.")
                    user = client.get_channel(813872172799754250)
                    modnotice = f"`{message.author.name}` queried the Bot."
                    await user.send(modnotice)
                    session.append(message.author.name)
                    for sessions in session:
                        print(sessions)

@client.event
async def on_member_join(member):
  role = get(member.guild.roles, id=806522859342135298)
  await member.add_roles(role)
  await member.send("Sample Text")

client.run('TOKEN')
