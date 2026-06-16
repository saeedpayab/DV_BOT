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
BOT_TOKEN = "اینجا-باید-توکن-رو-وارد-کنی"
CHANNEL_ID = "@v2r_plus"
DELETE_AFTER_SECONDS = 60  # پاک شدن فایل از سرور بعد از ۶۰ ثانیه
# =================================================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def check_membership(user_id: int, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """بررسی عضویت کاربر در کانال"""
    try:
        member = await context.bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception:
        return False


async def delete_file_later(filepath: str, delay: int):
    """پاک کردن فایل از سرور بعد از تاخیر مشخص"""
    await asyncio.sleep(delay)
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            logger.info(f"✅ فایل پاک شد: {filepath}")
    except Exception as e:
        logger.error(f"خطا در پاک کردن فایل: {e}")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """هندلر دستور /start"""
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
    """بررسی عضویت بعد از کلیک روی دکمه"""
    query = update.callback_query
    await query.answer()

    user = query.from_user
    is_member = await check_membership(user.id, context)

    if is_member:
        await query.edit_message_text(
            "✅ عضویت تأیید شد!\n\n"
            "🎬 *ربات دانلودر ویدیو*\n\n"
            "حالا لینک ویدیو رو برام بفرست:\n\n"
            "✅ یوتیوب\n"
            "✅ اینستاگرام (Reels)\n"
            "✅ توییتر/X\n"
            "✅ تیک‌تاک\n"
            "✅ و خیلی سایت‌های دیگه!\n\n"
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
            "❌ هنوز عضو کانال نشدی!\n\n"
            "لطفاً اول در کانال عضو بشو بعد دکمه رو بزن 👇",
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
        # یوتیوب
        if "youtube.com" in url or "youtu.be" in url:
            ydl_opts = {
                "format": "best[ext=mp4]/best",
                "outtmpl": f"downloads/{user.id}_%(title).50s.%(ext)s",
                "quiet": True,
                "no_warnings": True,
                "cookiefile": r"C:\Users\Saeed Payab\Desktop\Bot\cookies.txt",
                "proxy": "socks5://127.0.0.1:10808",  # پورت VPN خودت رو بذار
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                title = info.get("title", "ویدیو")
                filename = ydl.prepare_filename(info)

        # اینستاگرام، تیک‌تاک، توییتر و بقیه
        else:
            ydl_opts = {
                "format": "best[ext=mp4]/best",
                "outtmpl": f"downloads/{user.id}_%(title).50s.%(ext)s",
                "quiet": True,
                "no_warnings": True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                title = info.get("title", "ویدیو")
                filename = ydl.prepare_filename(info)

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

    finally:
        # اگه آپلود موفق نبود فایل رو همون لحظه پاک کن
        if filename and os.path.exists(filename):
            # فقط اگه task پاک‌سازی ست نشده باشه
            pass


def main():
    from telegram.ext import ApplicationBuilder
    import httpx

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
