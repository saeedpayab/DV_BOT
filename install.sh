#!/bin/bash

# ==========================================
#   نصب خودکار ربات دانلودر تلگرام
# ==========================================

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}"
echo "╔═══════════════════════════════════════╗"
echo "║     ربات دانلودر ویدیو تلگرام        ║"
echo "║          نصب خودکار                   ║"
echo "╚═══════════════════════════════════════╝"
echo -e "${NC}"

# گرفتن توکن ربات
echo -e "${YELLOW}لطفاً توکن ربات تلگرام را وارد کنید:${NC}"
echo -e "${BLUE}(توکن را از @BotFather دریافت کنید)${NC}"
read -p "توکن: " BOT_TOKEN

if [ -z "$BOT_TOKEN" ]; then
    echo -e "${RED}❌ توکن نمیتواند خالی باشد!${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}✅ شروع نصب...${NC}"
echo ""

# آپدیت سیستم
echo -e "${YELLOW}📦 آپدیت سیستم...${NC}"
apt-get update -qq
apt-get upgrade -y -qq

# نصب Python و pip
echo -e "${YELLOW}🐍 نصب Python...${NC}"
apt-get install -y -qq python3 python3-pip python3-venv

# نصب ffmpeg برای merge ویدیو و صدا
echo -e "${YELLOW}🎬 نصب ffmpeg...${NC}"
apt-get install -y -qq ffmpeg

# نصب Deno برای yt-dlp
echo -e "${YELLOW}🦕 نصب Deno...${NC}"
curl -fsSL https://deno.land/install.sh | sh -s -- --no-modify-path 2>/dev/null
export DENO_INSTALL="/root/.deno"
export PATH="$DENO_INSTALL/bin:$PATH"
echo 'export DENO_INSTALL="/root/.deno"' >> /root/.bashrc
echo 'export PATH="$DENO_INSTALL/bin:$PATH"' >> /root/.bashrc

# ساخت پوشه پروژه
echo -e "${YELLOW}📁 ساخت پوشه پروژه...${NC}"
mkdir -p /opt/telegram-bot/downloads
cd /opt/telegram-bot

# ساخت virtual environment
python3 -m venv venv
source venv/bin/activate

# نصب کتابخونه‌ها
echo -e "${YELLOW}📚 نصب کتابخونه‌های Python...${NC}"
pip install -q --upgrade pip
pip install -q python-telegram-bot yt-dlp pytubefix

# ساخت فایل bot.py
echo -e "${YELLOW}📝 ساخت فایل ربات...${NC}"
cat > /opt/telegram-bot/bot.py << BOTEOF
import os
import asyncio
import logging
import yt_dlp
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes,
)

BOT_TOKEN = "${BOT_TOKEN}"
CHANNEL_ID = "@v2r_plus"
DELETE_AFTER_SECONDS = 60

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def check_membership(user_id: int, context: ContextTypes.DEFAULT_TYPE) -> bool:
    try:
        member = await context.bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception:
        return False


async def delete_file_later(filepath: str, delay: int):
    await asyncio.sleep(delay)
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            logger.info(f"✅ فایل پاک شد: {filepath}")
    except Exception as e:
        logger.error(f"خطا در پاک کردن فایل: {e}")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    is_member = await check_membership(user.id, context)

    if not is_member:
        keyboard = [
            [InlineKeyboardButton("📢 عضویت در کانال", url="https://t.me/v2r_plus")],
            [InlineKeyboardButton("✅ عضو شدم!", callback_data="check_membership")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            f"👋 سلام {user.first_name}!\n\n"
            "برای استفاده از ربات، ابتدا باید در کانال ما عضو بشی 👇",
            reply_markup=reply_markup,
        )
        return

    await update.message.reply_text(
        f"👋 سلام {user.first_name}! خوش اومدی!\n\n"
        "🎬 *ربات دانلودر ویدیو*\n\n"
        "فقط لینک ویدیو رو برام بفرست تا دانلودش کنم:\n\n"
        "✅ یوتیوب (YouTube)\n"
        "✅ اینستاگرام (Reels & Posts)\n"
        "✅ توییتر/X\n"
        "✅ تیک‌تاک (TikTok)\n"
        "✅ و خیلی سایت‌های دیگه!\n\n"
        "⚠️ بعد از ارسال ویدیو، ۶۰ ثانیه فرصت داری تا سیوش کنی!\n\n"
        "📎 کافیه لینک رو اینجا بفرستی...",
        parse_mode="Markdown",
    )


async def check_membership_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user = query.from_user
    is_member = await check_membership(user.id, context)

    if is_member:
        await query.edit_message_text(
            "✅ عضویت تأیید شد!\n\n"
            "🎬 *ربات دانلودر ویدیو*\n\n"
            "حالا لینک ویدیو رو برام بفرست!\n\n"
            "⚠️ بعد از ارسال ویدیو، ۶۰ ثانیه فرصت داری تا سیوش کنی!",
            parse_mode="Markdown",
        )
    else:
        keyboard = [
            [InlineKeyboardButton("📢 عضویت در کانال", url="https://t.me/v2r_plus")],
            [InlineKeyboardButton("✅ عضو شدم!", callback_data="check_membership")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "❌ هنوز عضو کانال نشدی!\n\nلطفاً اول در کانال عضو بشو بعد دکمه رو بزن 👇",
            reply_markup=reply_markup,
        )


async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    is_member = await check_membership(user.id, context)

    if not is_member:
        keyboard = [
            [InlineKeyboardButton("📢 عضویت در کانال", url="https://t.me/v2r_plus")],
            [InlineKeyboardButton("✅ عضو شدم!", callback_data="check_membership")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            "⛔ برای استفاده از ربات باید عضو کانال ما بشی 👇",
            reply_markup=reply_markup,
        )
        return

    url = update.message.text.strip()

    if not url.startswith(("http://", "https://")):
        await update.message.reply_text("❌ لطفاً یک لینک معتبر بفرست!")
        return

    status_msg = await update.message.reply_text("⏳ در حال دانلود ویدیو... لطفاً صبر کن")
    os.makedirs("downloads", exist_ok=True)
    filename = None

    try:
        ydl_opts = {
            "format": "best[ext=mp4]/best",
            "outtmpl": f"downloads/{user.id}_%(title).50s.%(ext)s",
            "quiet": True,
            "no_warnings": True,
            "nocheckcertificate": True,
            "retries": 5,
            "fragment_retries": 5,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get("title", "ویدیو")
            filename = ydl.prepare_filename(info)
            if not os.path.exists(filename):
                filename = filename.rsplit(".", 1)[0] + ".mp4"

        file_size_mb = os.path.getsize(filename) / (1024 * 1024)
        await status_msg.edit_text(f"📤 در حال آپلود... ({file_size_mb:.1f} MB)")

        with open(filename, "rb") as video_file:
            await update.message.reply_video(
                video=video_file,
                caption=(
                    f"🎬 {title}\n\n"
                    f"⚠️ این ویدیو بعد از ۶۰ ثانیه از سرور پاک میشه!\n"
                    f"همین الان سیوش کن 👇\n\n"
                    f"🤖 @v2r_plus"
                ),
                supports_streaming=True,
                read_timeout=300,
                write_timeout=300,
                connect_timeout=60,
            )

        await status_msg.delete()
        asyncio.create_task(delete_file_later(filename, DELETE_AFTER_SECONDS))

        await update.message.reply_text(
            "⏱ *توجه!*\n\nویدیو ارسال شد ✅\n"
            "فایل بعد از *۶۰ ثانیه* از سرور پاک میشه.\n"
            "همین الان توی Saved Messages سیوش کن! 💾",
            parse_mode="Markdown",
        )

    except Exception as e:
        logger.error(f"Error: {e}")
        await status_msg.edit_text("❌ خطا در دانلود! لینک رو چک کن و دوباره امتحان کن.")
        if filename and os.path.exists(filename):
            os.remove(filename)


def main():
    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .connect_timeout(60)
        .read_timeout(300)
        .write_timeout(300)
        .pool_timeout(300)
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check_membership_callback, pattern="check_membership"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))

    logger.info("🤖 ربات شروع به کار کرد...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
BOTEOF

# ساخت service برای systemd
echo -e "${YELLOW}⚙️ ساخت سرویس systemd...${NC}"
cat > /etc/systemd/system/telegram-bot.service << SERVICEEOF
[Unit]
Description=Telegram Video Downloader Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/telegram-bot
Environment="DENO_INSTALL=/root/.deno"
Environment="PATH=/root/.deno/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
ExecStart=/opt/telegram-bot/venv/bin/python bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
SERVICEEOF

# فعال کردن و اجرای سرویس
echo -e "${YELLOW}🚀 راه‌اندازی سرویس...${NC}"
systemctl daemon-reload
systemctl enable telegram-bot
systemctl start telegram-bot

sleep 2

# چک کردن وضعیت
if systemctl is-active --quiet telegram-bot; then
    echo ""
    echo -e "${GREEN}╔═══════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║     ✅ نصب با موفقیت انجام شد!       ║${NC}"
    echo -e "${GREEN}╚═══════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${BLUE}دستورات مفید:${NC}"
    echo -e "  وضعیت ربات:  ${YELLOW}systemctl status telegram-bot${NC}"
    echo -e "  لاگ ربات:    ${YELLOW}journalctl -u telegram-bot -f${NC}"
    echo -e "  ری‌استارت:   ${YELLOW}systemctl restart telegram-bot${NC}"
    echo -e "  متوقف کردن: ${YELLOW}systemctl stop telegram-bot${NC}"
else
    echo -e "${RED}❌ مشکلی در راه‌اندازی سرویس پیش اومد!${NC}"
    echo -e "لاگ رو چک کن: ${YELLOW}journalctl -u telegram-bot -n 50${NC}"
fi
