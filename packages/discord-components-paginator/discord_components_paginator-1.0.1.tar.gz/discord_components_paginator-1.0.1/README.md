# discord-components Button Paginator

## Example

```py
from discord_components_paginator import Paginator, PaginatorStyle

...

@bot.command()
async def paginator_command(ctx):
  embeds = [
    discord.Embed(title=f"Page {page}") for page in range(1, 6)
  ]
  paginator = Paginator(bot, ctx, PaginatorStyle.FIVE_BUTTONS_WITH_COUNT, embeds)
  await paginator.start()
```
