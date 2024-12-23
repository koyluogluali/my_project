

import discord
from discord.ext import commands
from bot_token import bot_token
from keras_code import detected_valorant_agents
import os
from ajan_sözlük import detected_valorant_agents

# Discord intents ve bot ayarları
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Bot hazır olduğunda bir mesaj yaz
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Basit bir merhaba komutu
@bot.command()
async def merhaba(ctx):
    await ctx.send(f'selam ben bir botum {bot.user}!')

# "he" komutu
@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

# Valorant ajanlarını algılama komutu
@bot.command()
async def detect(ctx):
    if ctx.message.attachments:
        await ctx.send(f'Algılama başladı!')

        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_path = f"images/{file_name}"

            # Fotoğraf kaydetme
            await attachment.save(file_path)

            # Dosya formatı kontrolü (sadece resimler)
            if not file_name.endswith(('png', 'jpg', 'jpeg', 'gif')):
                await ctx.send(f"Geçersiz dosya formatı! Lütfen bir resim dosyası yükleyin.")

            # Model ile tahmin yapma
            classname, score = detected_valorant_agents(
            file_path,  
            "converted_keras/keras_model.h5", 
            "converted_keras/labels.txt"
            )
            print(classname)
            await ctx.send(f'Tahmin edilen ajan: {classname} (Güven Skoru: {score:.2f})')
            
            

            # Dosya kaydedildi mesajı
            await ctx.send(f'Dosya kaydedildi ve işleme alındı!')

    else:
        await ctx.send(f'Bu komutla birlikte bir fotoğraf da yüklemelisiniz!')
        
    if classname == 'neon':
        await ctx.send("""Düellocu rolündeki bu karakter elektro ok ile düşmanlarını sersemletir,
yüksek devir ile daha hızlı yol alır,
hız şeridi ile hem görüşü engelleyen hem de düşmana hasar veren duvar örer ve ulti yeteneği ile düşmanlarına ölümcül saldırılar yapar.""")
    if classname == 'yoru':
        await ctx.send("""Yoru’nun uzmanlığı düşmanlarını farklı şekillerde kandırabilmesi.
Bir boyut parçacığını koparıp fırlattığı kör nokta ile düşmanlarını kör ediyor.
Bir boyut geçidi küresi kuşandığı çatkapı ile küreyi konumlandırdığı yere ışınlanıyor.
Düşmanları kandırmak için kullandığı fake at ile istediği yöne ve noktaya doğru ayak sesi çıkmasını sağlıyor.
Ulti yeteneği boyutlararası geçiş ise onu düşmanları tarafından hem görünmez, hem de etkilenmez hale getiriyor.""")
    if  classname == 'chamber':
        await ctx.send("""Gözcü rolündeki bu karakter kelle avcısı ile ağır bir tabanca kuşanır, 
        buluşma ile belli bir noktaya ışınlanabilir, 
        kartvizit ile düşmanlarını yavaşlatır ve ulti yeteneği ile öldürücü bir keskin nişancı tüfeği kuşanır.""")
    elif  classname == 'cypher':
        await ctx.send("""Düşmanın nerede olduğunu tespit etmek için doğmuş Cypher. 
        Etkili şekilde kullanabilmek için bol antrenman isteyen ajanın siber kafes yeteneği sayesinde görüşü engelleyen ve düşmanı içine hapseden dairesel alanlar oluşturuluyor. Hedef alınan noktaya yerleştirilen gizli kamera sayesinde düşmanları gözlemlemek, hatta işaretleyici iğne atmak mümkün.
        Atıldığı noktadan karşıya hat çeken bubi tuzağı, yakalanan rakibi sarsıp görünür kılıyor. Ulti yeteneği nöron hırsızı ise ölen bir düşmanı kullanarak, adeta sorgulayarak diğer düşmanların konumunu ortaya çıkarıyor.""")

    elif  classname == 'raze':("""Oyunun kapalı beta sürecinde en çok tartışma yaratan ajan Raze olmuştu.
Bunun nedeni ise Valorant’ın temel yapısına aykırı özellikleri.
Tamamı hasar vermeye yönelik yeteneklere sahip Raze’in patlayıcı çantası düşmana hasar verirken, kendisini yukarı fırlatıyor.
Kullanım şekli kısıtlanan renk tesirli bomba ile düşmanlar kolayca avlanıyor. Gördüğü düşmana odaklanan ve vurulmadığı takdirde kolayca skor alabilen bombot yüzünden rakipler paniğe kapılabiliyor.
Ultisi ise bir hamlede “ace” aldırabilen nefes kesen (roketatar) ki tüm bu özellikler bir araya geldiğinde oynaması en kolay karakterlerden biri sayılabilir Raze.""")


    elif  classname == 'brimstone':("""Oyuna yeni başlayan herkesin ilk tercihi olması gereken bir ajan.
Bunun nedeni yeteneklerinin hem kolay kullanılması, hem de gayet etkili olması.
İlk olarak yakıcı özelliği sayesinde kısa süreliğine belli bir zemini alevle kaplıyor.
Takıma hareket alanı sağlayan dumanlı hava sahası ile ayrı ayrı ya da eş zamanlı olarak üç duman bulutu atıyor.
Yere bıraktığı kuvvet işareti sayesinde silahların atış hızını artırıyor.
Ultisi uydu saldırısı ise belli bir alandaki düşmanlara lazerle yüksek miktarda hasar veriyor.""")


    elif  classname == 'jett':("""Oyundaki en hareketli karakter olan Jett’i kontrol edebilmek ve etkili kullanabilmek uzmanlık gerektiriyor.
Ona hareket kabiliyeti veren özelliklerden hafifle ile havaya sıçramak, rüzgar gibi ile hareket edilen yöne ya da ileriye atılmak mümkün.
Bu özellikler rakibin görüşünü engelleyen duman bulutu ile beraber kullanıldığında bir hayli etkili oluyor.
Jett’in ultisi keskin fırtına ise ona fırlatılabilir beş bıçak veriyor. Bıçaklar tek tek ya da topluca atılabiliyor ve bir düşmanı öldürünce yenileniyor.
Nişan alma kabiliyetine fazlasıyla güvenenler için ideal.""")

    elif  classname == 'phonix':("""Oynaması en eğlenceli karakterlerden biri Phoenix ancak onu etkili şekilde kullanmak için biraz pratik gerekiyor.
Düellocu rolündeki bu karakterin ördüğü ateşten duvar ile hem görüş engelleniyor, hem de duvara temas eden düşmana hasar veriliyor.
Sola ve sağa fırlatılabilen falso ile düşmanlar kısa süreliğine kör edilirken, atıldığı zeminde belli bir süre kalarak düşmana hasar veren yakar top düşmanı durdurmak için bire bir.
Phoenix’i eğlenceli kılan yakardöner ultisi ise kontrol edilebilir bir klon yaratarak kısa süreliğine adeta iki kişilik oynamayı mümkün kılıyor.""")
        
    
    elif  classname == 'sage ':("""""")

    elif  classname == 'sova':("""""")

    elif  classname == 'breach':("""""")

    elif  classname == 'omen':("""""")

    elif  classname == 'reyna':("""""")

    elif  classname == 'viper':("""""")

    elif  classname == 'killjoy':("""""")

    elif  classname == 'skye':("""""")

    elif  classname == 'astra':("""""")

    elif  classname == 'skye':("""""")
        
# Botu başlatma
bot.run(bot_token)