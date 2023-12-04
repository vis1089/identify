import discord
from discord.ext import commands
import cv2
import pytesseract

# Set up the Discord bot
bot = commands.Bot(command_prefix='!')

# Event to handle when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command to identify and type text from an image
@bot.command()
async def identify(ctx, *, image_url):
    # Download the image
    image_path = 'temp_image.jpg'
    await download_image(image_url, image_path)

    # Perform OCR on the image
    text = identify_text(image_path)

    # Send the identified text to the Discord channel
    await ctx.send(f"Identified Text:\n```{text}```")

# Function to download an image from a URL
async def download_image(url, file_path):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(file_path, 'wb') as file:
                file.write(await response.read())

# Function to identify text from an image using Tesseract OCR
def identify_text(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

# Replace 'your_token_here' with your actual Discord bot token
bot.run('your_token_here')
