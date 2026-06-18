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

# ==================== تنظیمات ====================
BOT_TOKEN = "Token-Ro-Vard-Kon"
CHANNEL_ID = "@v2r_plus"
DELETE_AFTER_SECONDS = 60
COOKIE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cookies.txt")
# =================================================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

if os.path.exists(COOKIE_FILE):
    logger.info(f"✅ فایل کوکی پیدا شد: {COOKIE_FILE}")
else:
    logger.warning(f"⚠️ فایل کوکی پیدا نشد: {COOKIE_FILE}")


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
        await update.message.reply_text(
            f"👋 سلام {user.first_name}!\n\n"
            "برای استفاده از ربات، ابتدا باید در کانال ما عضو بشی 👇",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        return

    await update.message.reply_text(
        f"👋 سلام {user.first_name}! خوش اومدی!\n\n"
        "🎬 *ربات دانلودر ویدیو*\n\n"
        "فقط لینک ویدیو رو برام بفرست:\n\n"
        "✅ یوتیوب (YouTube)\n"
        "✅ اینستاگرام (Reels & Posts)\n"
        "✅ توییتر/X\n"
        "✅ تیک‌تاک (TikTok)\n"
        "✅ و خیلی سایت‌های دیگه!\n\n"
        "⚠️ بعد از ارسال ویدیو، ۶۰ ثانیه فرصت داری تا سیوش کنی!",
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
            "حالا لینک ویدیو رو برام بفرست! 🎬\n\n"
            "⚠️ بعد از ارسال ویدیو، ۶۰ ثانیه فرصت داری تا سیوش کنی!",
        )
    else:
        keyboard = [
            [InlineKeyboardButton("📢 عضویت در کانال", url="https://t.me/v2r_plus")],
            [InlineKeyboardButton("✅ عضو شدم!", callback_data="check_membership")],
        ]
        await query.edit_message_text(
            "❌ هنوز عضو کانال نشدی!\n\nلطفاً اول عضو بشو بعد دکمه رو بزن 👇",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )


async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    is_member = await check_membership(user.id, context)

    if not is_member:
        keyboard = [
            [InlineKeyboardButton("📢 عضویت در کانال", url="https://t.me/v2r_plus")],
            [InlineKeyboardButton("✅ عضو شدم!", callback_data="check_membership")],
        ]
        await update.message.reply_text(
            "⛔ برای استفاده از ربات باید عضو کانال ما بشی 👇",
            reply_markup=InlineKeyboardMarkup(keyboard),
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
            "format": "18/best[ext=mp4]/best",
            "outtmpl": f"downloads/{user.id}_%(title).50s.%(ext)s",
            "quiet": True,
            "no_warnings": True,
            "nocheckcertificate": True,
            "retries": 5,
            "fragment_retries": 5,
            "cookiefile": COOKIE_FILE if os.path.exists(COOKIE_FILE) else None,
            "extractor_args": {"youtube": {"player_client": ["tv"]}},
            "remote_components": ["ejs:github"],
        }

        if os.path.exists(COOKIE_FILE):
            ydl_opts["cookiefile"] = COOKIE_FILE

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
