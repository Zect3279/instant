# start.py

import discord
from discord.ext import commands

import json
import random
import asyncio
import os
import sys
from dispander import dispand
import requests


global anser
anser = False

# vq.cmdから渡された引数を格納したリストの取得
argvs = sys.argv


class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.gui = ""


    @commands.Cog.listener()
    async def on_ready(self):
        print('Instant is Ready!')


    @commands.Cog.listener()
    async def on_message(self, message):

        await dispand(message)

        if message.content == "マリカ":
            await message.channel.send("""\
「リスカ」ってゅぅのゎ。。
逆から読むと「カスリ」。。
リスカしたのにかすっただけ。。
もぅﾏﾁﾞ無理。。
ﾘｽｶしょ。。
ぁ、かすった。。
男子にぃぢめられた。。
しょせんゥチゎィきてるぃみなぃってこと？
もぅﾏﾁﾞ無理。
今ＤＳの電源ぃれた。
ﾏﾘｶしょ･･･
ﾌﾞｫｫｫｫｫｫｫｫｫﾝｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｲｲｨｨｨｲｲﾔｯﾋｨｨｨｨｲｲｲｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗ
            """)

        if message.content == "え？？？.":

            # await asyncio.sleep(20)

            embed=discord.Embed(title="警告 : 外部アクセス検知", description="サーバー間を移動するとIDを剥奪されます。Discord本社にレポートを送信するまで移動しないでください。", color=0xff0000)
            embed.add_field(name="以下のサーバーからアクセスを検知しました", value=message.guild.name + " (IP: 192.168.45.3)", inline=False)
            embed.add_field(name="ID", value="`" + str(message.id) + "`", inline=True)
            await message.channel.send(embed=embed)

            # webhook_url = 'https://discord.com/api/webhooks/806744852058079272/GdfWBywP59tzuOrgN8JAh1eByi75Yl9ko1hzu2-MjrH8DX_hjDG7XtyhXVC_dfvYGa5h'
            #
            # main_content = {
            #     "username": "Groovy",
            #     "avatar_url": "https://assets.groovy.bot/groovy_rounded.png",
            #     "embeds": [
            #     {
            #         "title": "警告 : 外部アクセス検知",
            #         "description": "サーバー間を移動するとIDを剥奪されます。Discord本社にレポートを送信するまで移動しないでください。",
            #         "color": 0xffff00,
            #         "fields": [
            #             {
            #             "name": "以下のサーバーからアクセスを検知しました",
            #             "value": f"{gui} (IP: 192.168.45.3)",
            #             "inline": False
            #             },
            #             {
            #             "name": "ID",
            #             "value": f"`{ctx.message.id}`",
            #             "inline": True
            #             }
            #         ]
            #     }
            #     ]
            # }
            # requests.post(webhook_url,json.dumps(main_content),headers={'Content-Type': 'application/json'})
    # async def create_channel(ctx):
    #     category_id = ctx.author.channel.category_id
    #     category = ctx.author.guild.get_channel(category_id)
    #     new_channel = await category.create_text_channel("test")
    #     return new_channel


    @commands.command()
    async def instant(self,ctx, *ins):

        # if ctx.author != self.bot.get_user(653785595075887104):
        #     await ctx.send("あなたには使用する権限がありません。 \nYou don't have the privilege to use this.")
        #     return

        if not ins:
            await ctx.send("インスタント名を指定してください。\n`/instant [インスタント名]`")
            return
        await ctx.send(f"{ins[0]} を展開します。")

        if ins[0] == "問題行為":
            for chan in ctx.guild.channels:
                await chan.delete()

            for rol in all_role:
                try:
                    await rol.delete()
                except:
                    a = "a"
            channel = await ctx.guild.create_text_channel("無題のテキストチャンネル")
            # チャンネルのリンクと作成メッセージを送信
            text = f"{ins[0]} の展開が完了しました。"
            await channel.send(text)

        if ins[0] == "カテゴリー作成":
            category = await ctx.guild.create_category(name=ins[1])
            category = ctx.guild.get_channel(category_id)
            await category.create_text_channel(ins[2])
            voice = await category.create_voice_channel(ins[2])
            await voice.edit(user_limit=50)
            # チャンネルのリンクと作成メッセージを送信
            text = f"{ins[0]} の実行が完了しました。"
            await ctx.send(text)

        if ins[0] == "チャンネル作成":
            category_id = ctx.channel.category_id
            category = ctx.guild.get_channel(category_id)
            await category.create_text_channel(ins[1])
            voice = await category.create_voice_channel(ins[1])
            await voice.edit(user_limit=50)
            # チャンネルのリンクと作成メッセージを送信
            text = f"{ins[0]} の実行が完了しました。"
            await ctx.send(text)

        if ins[0] == "テキスト作成":
            category_id = ctx.channel.category_id
            category = ctx.guild.get_channel(category_id)
            await category.create_text_channel(ins[1])
            # チャンネルのリンクと作成メッセージを送信
            text = f"{ins[0]} の実行が完了しました。"
            await ctx.send(text)

        if ins[0] == "ボイス作成":
            category_id = ctx.channel.category_id
            category = ctx.guild.get_channel(category_id)
            voice = await category.create_voice_channel(ins[1])
            await voice.edit(user_limit=50)
            # チャンネルのリンクと作成メッセージを送信
            text = f"{ins[0]} の実行が完了しました。"
            await ctx.send(text)

        if ins[0] == "labo":
            category = await ctx.guild.create_category(name="研究所")
            chan = await category.create_text_channel("bot研究室")
            voice = await category.create_voice_channel("会議室")
            await voice.edit(user_limit=50)
            role = await ctx.guild.create_role(name="研究員",colour=discord.Colour.from_rgb(0, 255, 255))
            text = f"{ins[0]} の実行が完了しました。"
            await ctx.send(text)
            await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
            await chan.set_permissions(ctx.author,read_messages=True)
            # await chan.set_permissions(role,read_messages=True)
            await voice.set_permissions(ctx.guild.roles[0],read_messages=False)
            await voice.set_permissions(ctx.author,read_messages=True)
            # await voice.set_permissions(role,read_messages=True)


        if ins[0] == "自由部屋2":
            category = await ctx.guild.create_category(name="自由部屋Ⅱ",position=2)
            await category.create_text_channel("自由部屋①")
            await category.create_text_channel("自由部屋②")
            await category.create_text_channel("自由部屋③")
            voice = await category.create_voice_channel("自由部屋①")
            await voice.edit(user_limit=50)
            voice = await category.create_voice_channel("自由部屋②")
            await voice.edit(user_limit=50)
            voice = await category.create_voice_channel("自由部屋③")
            await voice.edit(user_limit=50)
            # チャンネルのリンクと作成メッセージを送信
            text = f"{ins[0]} の実行が完了しました。"
            await ctx.send(text)

        if ins[0] == "カテゴリー削除":
            for chan in ctx.channel.category.channels:
                await chan.delete()
            # await ctx.channel.delete()
            await ctx.channel.category.delete()

        # if ins[0] == "全削除":
        #     for chan in ctx.guild.channels:
        #         await chan.delete()
        #         text = f"{ins[0]} の実行が完了しました。"
        #         await ctx.send(text)

        if ins[0] == "あまなー界隈":
            for chan in ctx.guild.channels:
                await chan.delete()

            await ctx.guild.create_text_channel("welcome")
            await ctx.guild.create_text_channel("掲示板")
            await ctx.guild.create_text_channel("timeline")
            await ctx.guild.create_text_channel("各種宣伝")

            category = await ctx.guild.create_category(name="総合")
            await category.create_text_channel("総合チャット")
            voice = await category.create_voice_channel("総合チャット")
            await voice.edit(user_limit=99)

            category = await ctx.guild.create_category(name="自由部屋")
            await category.create_text_channel("自由部屋①")
            await category.create_text_channel("自由部屋②")
            await category.create_text_channel("自由部屋③")
            voice = await category.create_voice_channel("自由部屋①")
            await voice.edit(user_limit=50)
            voice = await category.create_voice_channel("自由部屋②")
            await voice.edit(user_limit=50)
            voice = await category.create_voice_channel("自由部屋③")
            await voice.edit(user_limit=50)

            category = await ctx.guild.create_category(name="個通部屋")
            await category.create_text_channel("個通チャット")
            voice = await category.create_voice_channel("個通部屋①")
            await voice.edit(user_limit=50)
            voice = await category.create_voice_channel("個通部屋②")
            await voice.edit(user_limit=50)
            voice = await category.create_voice_channel("個通部屋③")
            await voice.edit(user_limit=50)

            category = await ctx.guild.create_category(name="Vocaleague")
            await category.create_text_channel("ボカリーグ会場")
            voice = await category.create_voice_channel("ボカリーグ会場")
            await voice.edit(user_limit=50)

            category = await ctx.guild.create_category(name="聴く")
            await category.create_text_channel("聴く！")
            voice = await category.create_voice_channel("聴く！")
            await voice.edit(user_limit=50)

            category = await ctx.guild.create_category(name="聴く２")
            await category.create_text_channel("聴く！２")
            voice = await category.create_voice_channel("聴く！２")
            await voice.edit(user_limit=50)

        if ins[0] == "修復":
            await ctx.guild.edit(name=self.gui)
            for chan in ctx.guild.channels:
                if chan == ctx.author.voice.channel:
                    print("a")
                elif chan == ctx.channel:
                    print("b")
                else:
                    await chan.set_permissions(ctx.guild.roles[0],read_messages=True)
            text = f"{ins[0]} の実行が完了しました。"
            await ctx.send(text)

        if ins[0] == "どっきり企画":
            self.gui = ctx.guild.name
            gui = ctx.guild.name
            vc = ctx.author.voice.channel
            for chan in ctx.guild.voice_channels:
                for mem in chan.members:
                    await mem.edit(voice_channel=vc)

            for chan in ctx.guild.channels:
                if chan == ctx.author.voice.channel:
                    print("a")
                elif chan == ctx.channel:
                    print("b")
                else:
                    await chan.set_permissions(ctx.guild.roles[0],read_messages=False)

            await ctx.guild.edit(name="谺｡蝗槭≠縺ｾ縺｡豁ｻ縺")

            webhook_url = 'https://discord.com/api/webhooks/806744852058079272/GdfWBywP59tzuOrgN8JAh1eByi75Yl9ko1hzu2-MjrH8DX_hjDG7XtyhXVC_dfvYGa5h'

            main_content = {
                "username": "Groovy",
                "avatar_url": "https://assets.groovy.bot/groovy_rounded.png",
                "embeds": [
                {
                    "title": "警告 : 外部アクセス検知",
                    "description": "サーバー間を移動するとIDを剥奪されます。Discord本社にレポートを送信するまで移動しないでください。",
                    "color": 0xffff00,
                    "fields": [
                        {
                        "name": "以下のサーバーからアクセスを検知しました",
                        "value": f"{gui} (IP: 192.168.45.3)",
                        "inline": False
                        },
                        {
                        "name": "ID",
                        "value": f"`{ctx.message.id}`",
                        "inline": True
                        }
                    ]
                }
                ]
            }

            requests.post(webhook_url,json.dumps(main_content),headers={'Content-Type': 'application/json'})

            main_content = {
                "username": "Rythm",
                "avatar_url": "https://rythmbot.co/assets/img/rythm.png",
                "embeds": [
                {
                    "title": "警告 : 外部アクセス検知",
                    "description": "サーバー間を移動するとIDを剥奪されます。Discord本社にレポートを送信するまで移動しないでください。",
                    "color": 0xff0000,
                    "fields": [
                        {
                        "name": "以下のサーバーからアクセスを検知しました",
                        "value": f"{gui} (IP: 192.168.45.3)",
                        "inline": False
                        },
                        {
                        "name": "ID",
                        "value": f"`{ctx.message.id}`",
                        "inline": True
                        }
                    ]
                }
                ]
            }
            requests.post(webhook_url,json.dumps(main_content),headers={'Content-Type': 'application/json'})

            main_content = {
                "username": "MathBot",
                "avatar_url": "https://images.discordapp.net/avatars/134073775925886976/970d33bddeb40f9b7a20f7524a6b07f5.png",
                "embeds": [
                {
                    "title": "警告 : 外部アクセス検知",
                    "description": "サーバー間を移動するとIDを剥奪されます。Discord本社にレポートを送信するまで移動しないでください。",
                    "color": 0x00bfff,
                    "fields": [
                        {
                        "name": "以下のサーバーからアクセスを検知しました",
                        "value": f"{gui} (IP: 192.168.45.3)",
                        "inline": False
                        },
                        {
                        "name": "ID",
                        "value": f"`{ctx.message.id}`",
                        "inline": True
                        }
                    ]
                }
                ]
            }
            requests.post(webhook_url,json.dumps(main_content),headers={'Content-Type': 'application/json'})
            text = f"{ins[0]} の実行が完了しました。"
            await ctx.send(text)




    @commands.command()
    async def hook(self,ctx):
        print("a")



    @commands.command()
    async def test(self,ctx):
        webhook_url = 'https://discord.com/api/webhooks/\
        806744852058079272/GdfWBywP59tzuOrgN8JAh1eByi75Yl9ko1hzu2-MjrH8DX_hjDG7XtyhXVC_dfvYGa5h'

        # main_content = {
        #     "username": "Rythm",
        #     "avatar_url": "https://rythmbot.co/assets/img/rythm.png",
        #     "content": "実験"
        # }
        # requests.post(webhook_url, main_content)
        #
        # main_content = {
        #     "username": "Groovy",
        #     "avatar_url": "https://assets.groovy.bot/groovy_rounded.png",
        #     "content": "実験"
        # }
        # requests.post(webhook_url, main_content)

        main_content = {
            "username": "MathBot",
            "avatar_url": "https://images.discordapp.net/avatars/134073775925886976/970d33bddeb40f9b7a20f7524a6b07f5.png",
            "content": "( ồωồ)و ｸﾞｯ!"
        }
        requests.post(webhook_url, main_content)
        print("done")




































def setup(bot):
    bot.add_cog(Game(bot))
