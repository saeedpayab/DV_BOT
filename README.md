<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>DV BOT — README Preview</title>
  <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css"/>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap');

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Inter', sans-serif;
      background: #0d1117;
      color: #e6edf3;
      min-height: 100vh;
    }

    /* ── Top bar ── */
    .topbar {
      background: #161b22;
      border-bottom: 1px solid #30363d;
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 100;
    }
    .topbar-logo {
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 700;
      font-size: 1.1rem;
      color: #e6edf3;
    }
    .topbar-logo span { color: #58a6ff; }
    .lang-tabs {
      display: flex;
      gap: 8px;
    }
    .lang-btn {
      padding: 6px 18px;
      border-radius: 20px;
      border: 1px solid #30363d;
      background: transparent;
      color: #8b949e;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: all .2s;
      font-family: 'Inter', sans-serif;
    }
    .lang-btn.active {
      background: #1f6feb;
      border-color: #1f6feb;
      color: #fff;
    }
    .lang-btn:hover:not(.active) {
      border-color: #58a6ff;
      color: #58a6ff;
    }

    /* ── Copy button ── */
    .copy-area {
      display: flex;
      justify-content: flex-end;
      padding: 16px 0 4px;
    }
    .copy-btn {
      display: flex;
      align-items: center;
      gap: 7px;
      padding: 8px 20px;
      border-radius: 8px;
      border: 1px solid #30363d;
      background: #21262d;
      color: #8b949e;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: all .2s;
      font-family: 'Inter', sans-serif;
    }
    .copy-btn:hover { border-color: #58a6ff; color: #58a6ff; background: #1c2128; }
    .copy-btn.copied { border-color: #3fb950; color: #3fb950; }

    /* ── Tab content wrapper ── */
    .tab-content { display: none; }
    .tab-content.active { display: block; }

    /* ── Main container ── */
    .container {
      max-width: 900px;
      margin: 0 auto;
      padding: 32px 20px 80px;
    }

    /* ── GitHub-style README card ── */
    .readme-card {
      background: #161b22;
      border: 1px solid #30363d;
      border-radius: 12px;
      overflow: hidden;
    }
    .readme-header {
      background: #21262d;
      border-bottom: 1px solid #30363d;
      padding: 12px 20px;
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.82rem;
      color: #8b949e;
    }
    .readme-header svg { color: #58a6ff; }
    .readme-body {
      padding: 36px 44px;
      line-height: 1.8;
    }

    /* ── MD Typography ── */
    .md h1 {
      font-size: 2rem;
      font-weight: 800;
      border-bottom: 1px solid #30363d;
      padding-bottom: 12px;
      margin-bottom: 20px;
      color: #e6edf3;
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .md h2 {
      font-size: 1.35rem;
      font-weight: 700;
      border-bottom: 1px solid #30363d;
      padding-bottom: 8px;
      margin: 36px 0 16px;
      color: #e6edf3;
    }
    .md h3 {
      font-size: 1.08rem;
      font-weight: 600;
      margin: 22px 0 10px;
      color: #cdd9e5;
    }
    .md p {
      color: #cdd9e5;
      margin-bottom: 14px;
      font-size: 0.97rem;
    }
    .md ul {
      padding-left: 22px;
      margin-bottom: 16px;
    }
    .md ul li {
      color: #cdd9e5;
      margin-bottom: 7px;
      font-size: 0.95rem;
    }
    .md ul li::marker { color: #58a6ff; }
    .md strong { color: #e6edf3; font-weight: 600; }
    .md a { color: #58a6ff; text-decoration: none; }
    .md a:hover { text-decoration: underline; }
    .md code {
      background: #1c2128;
      border: 1px solid #30363d;
      border-radius: 5px;
      padding: 2px 7px;
      font-family: 'Fira Code', monospace;
      font-size: 0.85rem;
      color: #ff7b72;
    }
    .md pre {
      background: #1c2128 !important;
      border: 1px solid #30363d;
      border-radius: 10px;
      padding: 18px 20px;
      overflow-x: auto;
      margin: 16px 0 20px;
      position: relative;
    }
    .md pre code {
      background: transparent !important;
      border: none !important;
      padding: 0 !important;
      font-size: 0.9rem;
      color: #e6edf3;
    }
    .md blockquote {
      border-left: 4px solid #1f6feb;
      background: #1c2128;
      padding: 12px 18px;
      border-radius: 0 8px 8px 0;
      margin: 16px 0;
      color: #8b949e;
      font-size: 0.93rem;
    }
    .md hr {
      border: none;
      border-top: 1px solid #30363d;
      margin: 28px 0;
    }
    .md table {
      width: 100%;
      border-collapse: collapse;
      margin: 16px 0 24px;
      font-size: 0.9rem;
    }
    .md th {
      background: #21262d;
      color: #e6edf3;
      font-weight: 600;
      padding: 10px 16px;
      border: 1px solid #30363d;
      text-align: left;
    }
    .md td {
      padding: 9px 16px;
      border: 1px solid #30363d;
      color: #cdd9e5;
    }
    .md tr:nth-child(even) td { background: #1c2128; }

    /* ── Badges ── */
    .badge-row {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin: 16px 0 24px;
    }
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: .3px;
    }
    .badge-blue   { background: #1f3a5f; border: 1px solid #1f6feb; color: #58a6ff; }
    .badge-green  { background: #1b3a2a; border: 1px solid #3fb950; color: #3fb950; }
    .badge-orange { background: #3d2400; border: 1px solid #f0883e; color: #f0883e; }
    .badge-purple { background: #2a1a4a; border: 1px solid #a371f7; color: #a371f7; }

    /* ── Feature cards ── */
    .feature-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 14px;
      margin: 20px 0 28px;
    }
    .feature-card {
      background: #1c2128;
      border: 1px solid #30363d;
      border-radius: 10px;
      padding: 18px 16px;
      transition: border-color .2s, transform .2s;
    }
    .feature-card:hover { border-color: #1f6feb; transform: translateY(-2px); }
    .feature-card .icon { font-size: 1.8rem; margin-bottom: 10px; }
    .feature-card h4 { font-size: 0.92rem; font-weight: 700; color: #e6edf3; margin-bottom: 6px; }
    .feature-card p  { font-size: 0.82rem; color: #8b949e; line-height: 1.55; }

    /* ── RTL section ── */
    .rtl { direction: rtl; text-align: right; font-family: 'Vazirmatn', 'Tahoma', 'Inter', sans-serif; }
    .rtl .md h1, .rtl .md h2, .rtl .md h3 { font-family: 'Vazirmatn', 'Tahoma', sans-serif; }
    .rtl .md ul { padding-right: 22px; padding-left: 0; }
    .rtl .md blockquote { border-left: none; border-right: 4px solid #1f6feb; border-radius: 8px 0 0 8px; }
    .rtl .badge-row { flex-direction: row-reverse; }
    .rtl .feature-grid { direction: rtl; }
    .rtl .md pre { direction: ltr; text-align: left; }

    /* ── Step box ── */
    .step-box {
      display: flex;
      align-items: flex-start;
      gap: 16px;
      background: #1c2128;
      border: 1px solid #30363d;
      border-radius: 10px;
      padding: 16px 20px;
      margin-bottom: 14px;
    }
    .step-num {
      width: 32px; height: 32px;
      background: #1f6feb;
      border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      font-weight: 800; font-size: 0.9rem; flex-shrink: 0;
      color: #fff;
    }
    .step-box .step-text { font-size: 0.92rem; color: #cdd9e5; padding-top: 5px; }
    .step-box .step-text strong { color: #e6edf3; display: block; margin-bottom: 4px; }

    /* ── Warning box ── */
    .warn-box {
      background: #2d1f00;
      border: 1px solid #f0883e;
      border-radius: 10px;
      padding: 14px 18px;
      display: flex; align-items: flex-start; gap: 10px;
      margin: 20px 0;
    }
    .warn-box p { color: #f0883e; font-size: 0.9rem; margin: 0; }

    /* ── Footer note ── */
    .footer-note {
      text-align: center;
      margin-top: 40px;
      color: #484f58;
      font-size: 0.8rem;
    }
  </style>
</head>
<body>

<!-- TOP BAR -->
<div class="topbar">
  <div class="topbar-logo">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#58a6ff" stroke-width="2">
      <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/>
      <polyline points="7 10 12 15 17 10"/>
      <line x1="12" y1="15" x2="12" y2="3"/>
    </svg>
    <span>DV</span> BOT — README
  </div>
  <div style="display:flex;align-items:center;gap:12px;">
    <div class="lang-tabs">
      <button class="lang-btn active" onclick="switchLang('en', this)">🇬🇧 English</button>
      <button class="lang-btn" onclick="switchLang('fa', this)">🇮🇷 فارسی</button>
    </div>
  </div>
</div>

<!-- CONTAINER -->
<div class="container">

  <!-- ── COPY BUTTON ── -->
  <div class="copy-area">
    <button class="copy-btn" id="copyBtn" onclick="copyMD()">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <rect x="9" y="9" width="13" height="13" rx="2"/>
        <path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/>
      </svg>
      Copy Markdown
    </button>
  </div>

  <!-- ══════════════════ ENGLISH ══════════════════ -->
  <div id="tab-en" class="tab-content active">
    <div class="readme-card">
      <div class="readme-header">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
        README.md
      </div>
      <div class="readme-body md" id="en-body">

        <h1>
          <span>📥</span> DV BOT
        </h1>

        <div class="badge-row">
          <span class="badge badge-blue">🤖 Telegram Bot</span>
          <span class="badge badge-green">✅ Ubuntu Ready</span>
          <span class="badge badge-orange">⚡ Fast &amp; Easy Install</span>
          <span class="badge badge-purple">🎬 Video Downloader</span>
        </div>

        <blockquote>
          A lightning-fast Telegram video downloader bot — just send a link, get your video instantly. Designed for Ubuntu servers with a one-command setup.
        </blockquote>

        <hr/>

        <h2>✨ Features</h2>

        <div class="feature-grid">
          <div class="feature-card">
            <div class="icon">▶️</div>
            <h4>YouTube Downloads</h4>
            <p>Send any YouTube link and receive a downloadable video file in seconds.</p>
          </div>
          <div class="feature-card">
            <div class="icon">📸</div>
            <h4>Instagram Downloads</h4>
            <p>Download reels, posts, and stories directly from Instagram links.</p>
          </div>
          <div class="feature-card">
            <div class="icon">𝕏</div>
            <h4>X (Twitter) Downloads</h4>
            <p>Grab videos from any X (formerly Twitter) post with a single message.</p>
          </div>
          <div class="feature-card">
            <div class="icon">⚡</div>
            <h4>Blazing Fast</h4>
            <p>Optimized for speed — videos are processed and delivered in no time.</p>
          </div>
          <div class="feature-card">
            <div class="icon">📲</div>
            <h4>Direct Download</h4>
            <p>Videos are sent with a download button directly inside Telegram.</p>
          </div>
          <div class="feature-card">
            <div class="icon">🔧</div>
            <h4>Zero Config</h4>
            <p>One command install — no complex configuration or dependencies to manage.</p>
          </div>
        </div>

        <hr/>

        <h2>🚀 Quick Installation</h2>

        <p>Install DV BOT on your Ubuntu server with a single command:</p>

        <pre><code class="language-bash">curl -sL "https://raw.githubusercontent.com/saeedpayab/DV_BOT/refs/heads/main/install.sh" | bash</code></pre>

        <h3>📋 Installation Steps</h3>

        <div class="step-box">
          <div class="step-num">1</div>
          <div class="step-text">
            <strong>Run the install command</strong>
            Copy and paste the curl command above into your Ubuntu terminal and press Enter.
          </div>
        </div>
        <div class="step-box">
          <div class="step-num">2</div>
          <div class="step-text">
            <strong>Enter your Telegram Bot Token</strong>
            The installer will prompt you to enter your Telegram bot token. Paste it and press Enter.
          </div>
        </div>
        <div class="step-box">
          <div class="step-num">3</div>
          <div class="step-text">
            <strong>Sit back &amp; relax 🎉</strong>
            Everything else is handled automatically. The bot will be up and running in moments.
          </div>
        </div>

        <div class="warn-box">
          <span style="font-size:1.2rem;">⚠️</span>
          <p><strong>Note:</strong> You need a valid Telegram bot token. Get one for free from <a href="https://t.me/BotFather" target="_blank">@BotFather</a> on Telegram before running the installer.</p>
        </div>

        <hr/>

        <h2>📖 How to Use</h2>

        <p>Using DV BOT is as simple as it gets:</p>

        <ul>
          <li>Open your Telegram bot</li>
          <li>Send a <strong>YouTube</strong>, <strong>Instagram</strong>, or <strong>X (Twitter)</strong> video link</li>
          <li>Wait a moment while the bot processes your request</li>
          <li>Receive the video file directly in Telegram with a <strong>download button</strong></li>
        </ul>

        <h3>🔗 Supported Platforms</h3>

        <table>
          <tr>
            <th>Platform</th>
            <th>Supported Content</th>
            <th>Status</th>
          </tr>
          <tr>
            <td>▶️ YouTube</td>
            <td>Videos, Shorts</td>
            <td>✅ Supported</td>
          </tr>
          <tr>
            <td>📸 Instagram</td>
            <td>Reels, Posts, Stories</td>
            <td>✅ Supported</td>
          </tr>
          <tr>
            <td>𝕏 X (Twitter)</td>
            <td>Video Tweets</td>
            <td>✅ Supported</td>
          </tr>
        </table>

        <hr/>

        <h2>⚙️ Requirements</h2>

        <ul>
          <li>Ubuntu Server (18.04 / 20.04 / 22.04 / 24.04)</li>
          <li>A valid Telegram Bot Token from <a href="https://t.me/BotFather">@BotFather</a></li>
          <li>Internet access on the server</li>
        </ul>

        <hr/>

        <h2>📄 License</h2>
        <p>This project is open-source. See the <a href="#">LICENSE</a> file for more details.</p>

        <hr/>

        <p style="text-align:center;color:#484f58;font-size:0.85rem;">
          Made with ❤️ by <a href="https://github.com/saeedpayab">saeedpayab</a>
        </p>

      </div>
    </div>
  </div>

  <!-- ══════════════════ PERSIAN ══════════════════ -->
  <div id="tab-fa" class="tab-content rtl">
    <div class="readme-card">
      <div class="readme-header" style="direction:rtl;">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
        README.md
      </div>
      <div class="readme-body md" id="fa-body">

        <h1>
          <span>📥</span> DV BOT
        </h1>

        <div class="badge-row">
          <span class="badge badge-blue">🤖 ربات تلگرام</span>
          <span class="badge badge-green">✅ سازگار با Ubuntu</span>
          <span class="badge badge-orange">⚡ نصب سریع</span>
          <span class="badge badge-purple">🎬 دانلودر ویدیو</span>
        </div>

        <blockquote>
          یک ربات تلگرامی فوق‌العاده سریع برای دانلود ویدیو — فقط لینک بفرست، ویدیو رو بگیر. طراحی‌شده برای سرورهای اوبونتو با نصب تک‌دستوری.
        </blockquote>

        <hr/>

        <h2>✨ قابلیت‌ها</h2>

        <div class="feature-grid" style="direction:rtl;">
          <div class="feature-card" style="text-align:right;">
            <div class="icon">▶️</div>
            <h4>دانلود از یوتیوب</h4>
            <p>هر لینک یوتیوبی بفرستی، ظرف چند ثانیه ویدیو با قابلیت دانلود دریافت می‌کنی.</p>
          </div>
          <div class="feature-card" style="text-align:right;">
            <div class="icon">📸</div>
            <h4>دانلود از اینستاگرام</h4>
            <p>دانلود ریلز، پست‌ها و استوری‌ها مستقیم از لینک اینستاگرام.</p>
          </div>
          <div class="feature-card" style="text-align:right;">
            <div class="icon">𝕏</div>
            <h4>دانلود از ایکس (توییتر)</h4>
            <p>ویدیوی هر توییتی رو با یک پیام ساده دریافت کن.</p>
          </div>
          <div class="feature-card" style="text-align:right;">
            <div class="icon">⚡</div>
            <h4>سرعت بی‌نظیر</h4>
            <p>بهینه‌شده برای سرعت — ویدیوها در کمترین زمان ممکن پردازش و ارسال می‌شن.</p>
          </div>
          <div class="feature-card" style="text-align:right;">
            <div class="icon">📲</div>
            <h4>دانلود مستقیم</h4>
            <p>ویدیو با دکمه دانلود مستقیم داخل تلگرام برات ارسال میشه.</p>
          </div>
          <div class="feature-card" style="text-align:right;">
            <div class="icon">🔧</div>
            <h4>بدون پیچیدگی</h4>
            <p>نصب با یک دستور — هیچ تنظیمات پیچیده‌ای نیاز نیست.</p>
          </div>
        </div>

        <hr/>

        <h2>🚀 نصب سریع</h2>

        <p>ربات DV BOT رو با یه دستور روی سرور اوبونتوت نصب کن:</p>

        <pre><code class="language-bash">curl -sL "https://raw.githubusercontent.com/saeedpayab/DV_BOT/refs/heads/main/install.sh" | bash</code></pre>

        <h3>📋 مراحل نصب</h3>

        <div class="step-box" style="direction:rtl;text-align:right;">
          <div class="step-num">۱</div>
          <div class="step-text">
            <strong>دستور نصب را اجرا کن</strong>
            دستور curl بالا رو کپی کن و توی ترمینال سرور اوبونتوت پیست کن و Enter بزن.
          </div>
        </div>
        <div class="step-box" style="direction:rtl;text-align:right;">
          <div class="step-num">۲</div>
          <div class="step-text">
            <strong>توکن ربات تلگرامت رو وارد کن</strong>
            اسکریپت نصب ازت می‌خواد توکن ربات تلگرامت رو وارد کنی. فقط توکن رو پیست کن و Enter بزن.
          </div>
        </div>
        <div class="step-box" style="direction:rtl;text-align:right;">
          <div class="step-num">۳</div>
          <div class="step-text">
            <strong>همه چیز خودکار انجام میشه 🎉</strong>
            بقیه مراحل نصب بطور کاملاً اتوماتیک انجام میشه. ربات چند لحظه دیگه آماده و فعاله!
          </div>
        </div>

        <div class="warn-box" style="direction:rtl;text-align:right;">
          <span style="font-size:1.2rem;">⚠️</span>
          <p><strong>توجه:</strong> برای نصب به یک توکن معتبر ربات تلگرام نیاز داری. قبل از اجرا، از <a href="https://t.me/BotFather" target="_blank">@BotFather</a> توکن بگیر.</p>
        </div>

        <hr/>

        <h2>📖 نحوه استفاده</h2>

        <p>استفاده از DV BOT خیلی ساده‌ست:</p>

        <ul>
          <li>ربات تلگرامت رو باز کن</li>
          <li>لینک ویدیو از <strong>یوتیوب</strong>، <strong>اینستاگرام</strong> یا <strong>ایکس (توییتر)</strong> بفرست</li>
          <li>چند لحظه صبر کن تا ربات لینک رو پردازش کنه</li>
          <li>ویدیو با <strong>دکمه دانلود</strong> مستقیم داخل تلگرام برات ارسال میشه</li>
        </ul>

        <h3>🔗 پلتفرم‌های پشتیبانی‌شده</h3>

        <table style="direction:rtl;">
          <tr>
            <th>پلتفرم</th>
            <th>محتوای پشتیبانی‌شده</th>
            <th>وضعیت</th>
          </tr>
          <tr>
            <td>▶️ YouTube</td>
            <td>ویدیو، شورتز</td>
            <td>✅ پشتیبانی می‌شه</td>
          </tr>
          <tr>
            <td>📸 Instagram</td>
            <td>ریلز، پست، استوری</td>
            <td>✅ پشتیبانی می‌شه</td>
          </tr>
          <tr>
            <td>𝕏 X (Twitter)</td>
            <td>توییت‌های ویدیویی</td>
            <td>✅ پشتیبانی می‌شه</td>
          </tr>
        </table>

        <hr/>

        <h2>⚙️ پیش‌نیازها</h2>

        <ul>
          <li>سرور Ubuntu (نسخه‌های 18.04 / 20.04 / 22.04 / 24.04)</li>
          <li>توکن معتبر ربات تلگرام از <a href="https://t.me/BotFather">@BotFather</a></li>
          <li>دسترسی به اینترنت از سرور</li>
        </ul>

        <hr/>

        <h2>📄 مجوز</h2>
        <p>این پروژه متن‌باز است. برای اطلاعات بیشتر فایل <a href="#">LICENSE</a> رو ببین.</p>

        <hr/>

        <p style="text-align:center;color:#484f58;font-size:0.85rem;">
          ساخته‌شده با ❤️ توسط <a href="https://github.com/saeedpayab">saeedpayab</a>
        </p>

      </div>
    </div>
  </div>

  <div class="footer-note">
    Preview rendered in GitHub Dark theme · Switch language above · Click "Copy Markdown" to copy the raw MD
  </div>
</div>

<script>
  // ── Syntax highlight ──
  document.addEventListener('DOMContentLoaded', () => hljs.highlightAll());

  // ── Language switcher ──
  function switchLang(lang, btn) {
    document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
    document.getElementById('tab-' + lang).classList.add('active');
    btn.classList.add('active');
    document.getElementById('copyBtn').textContent = lang === 'fa' ? ' کپی Markdown' : ' Copy Markdown';
    document.getElementById('copyBtn').innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg> ${lang === 'fa' ? 'کپی Markdown' : 'Copy Markdown'}`;
  }

  // ── Markdown strings ──
  const MD_EN = `# 📥 DV BOT

![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)
![Ubuntu](https://img.shields.io/badge/Ubuntu-Ready-orange?logo=ubuntu)
![License](https://img.shields.io/badge/License-MIT-green)

> A lightning-fast Telegram video downloader bot — just send a link, get your video instantly.  
> Designed for Ubuntu servers with a one-command setup.

---

## ✨ Features

| Feature | Description |
|---|---|
| ▶️ YouTube | Download any YouTube video or Short |
| 📸 Instagram | Download Reels, Posts & Stories |
| 𝕏 X (Twitter) | Download videos from any X post |
| ⚡ Blazing Fast | Videos processed and delivered instantly |
| 📲 Direct Download | Video sent with a download button in Telegram |
| 🔧 Zero Config | One-command install, fully automated setup |

---

## 🚀 Quick Installation

Run the following command on your Ubuntu server:

\`\`\`bash
curl -sL "https://raw.githubusercontent.com/saeedpayab/DV_BOT/refs/heads/main/install.sh" | bash
\`\`\`

### 📋 Installation Steps

1. **Run the install command** — paste the curl command into your Ubuntu terminal and press Enter.
2. **Enter your Telegram Bot Token** — the installer will prompt you. Just paste your token and press Enter.
3. **Sit back & relax 🎉** — everything else is handled automatically. The bot will be live in moments!

> ⚠️ **Note:** You need a valid Telegram bot token. Get one for free from [@BotFather](https://t.me/BotFather) before running the installer.

---

## 📖 How to Use

1. Open your Telegram bot
2. Send a **YouTube**, **Instagram**, or **X (Twitter)** video link
3. Wait a moment while the bot processes your request
4. Receive the video file with a **download button** directly in Telegram

### 🔗 Supported Platforms

| Platform | Supported Content | Status |
|---|---|---|
| ▶️ YouTube | Videos, Shorts | ✅ Supported |
| 📸 Instagram | Reels, Posts, Stories | ✅ Supported |
| 𝕏 X (Twitter) | Video Tweets | ✅ Supported |

---

## ⚙️ Requirements

- Ubuntu Server (18.04 / 20.04 / 22.04 / 24.04)
- A valid Telegram Bot Token from [@BotFather](https://t.me/BotFather)
- Internet access on the server

---

## 📄 License

This project is open-source. See the [LICENSE](LICENSE) file for more details.

---

<p align="center">Made with ❤️ by <a href="https://github.com/saeedpayab">saeedpayab</a></p>
`;

  const MD_FA = `<div dir="rtl">

# 📥 DV BOT

![ربات تلگرام](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)
![اوبونتو](https://img.shields.io/badge/Ubuntu-Ready-orange?logo=ubuntu)
![مجوز](https://img.shields.io/badge/License-MIT-green)

> یک ربات تلگرامی فوق‌العاده سریع برای دانلود ویدیو — فقط لینک بفرست، ویدیو رو بگیر.  
> طراحی‌شده برای سرورهای اوبونتو با نصب تک‌دستوری.

---

## ✨ قابلیت‌ها

| قابلیت | توضیح |
|---|---|
| ▶️ یوتیوب | دانلود هر ویدیو یا شورتز یوتیوب |
| 📸 اینستاگرام | دانلود ریلز، پست‌ها و استوری‌ها |
| 𝕏 ایکس (توییتر) | دانلود ویدیو از هر پست ایکس |
| ⚡ سرعت بی‌نظیر | پردازش و ارسال فوری ویدیو |
| 📲 دانلود مستقیم | ارسال ویدیو با دکمه دانلود داخل تلگرام |
| 🔧 بدون پیچیدگی | نصب با یک دستور، کاملاً اتوماتیک |

---

## 🚀 نصب سریع

دستور زیر رو روی سرور اوبونتوت اجرا کن:

\`\`\`bash
curl -sL "https://raw.githubusercontent.com/saeedpayab/DV_BOT/refs/heads/main/install.sh" | bash
\`\`\`

### 📋 مراحل نصب

1. **دستور نصب را اجرا کن** — دستور curl بالا رو توی ترمینال پیست کن و Enter بزن.
2. **توکن ربات تلگرامت رو وارد کن** — اسکریپت ازت می‌خواد. فقط توکن رو پیست کن و Enter بزن.
3. **همه چیز خودکار انجام میشه 🎉** — بقیه مراحل اتوماتیک است. ربات چند لحظه دیگه آماده‌ست!

> ⚠️ **توجه:** قبل از نصب، از [@BotFather](https://t.me/BotFather) توکن ربات تلگرام بگیر.

---

## 📖 نحوه استفاده

1. ربات تلگرامت رو باز کن
2. لینک ویدیو از **یوتیوب**، **اینستاگرام** یا **ایکس (توییتر)** بفرست
3. چند لحظه صبر کن تا ربات لینک رو پردازش کنه
4. ویدیو با **دکمه دانلود** مستقیم داخل تلگرام برات ارسال میشه

### 🔗 پلتفرم‌های پشتیبانی‌شده

| پلتفرم | محتوای پشتیبانی‌شده | وضعیت |
|---|---|---|
| ▶️ YouTube | ویدیو، شورتز | ✅ پشتیبانی می‌شه |
| 📸 Instagram | ریلز، پست، استوری | ✅ پشتیبانی می‌شه |
| 𝕏 X (Twitter) | توییت‌های ویدیویی | ✅ پشتیبانی می‌شه |

---

## ⚙️ پیش‌نیازها

- سرور Ubuntu (نسخه‌های 18.04 / 20.04 / 22.04 / 24.04)
- توکن معتبر ربات تلگرام از [@BotFather](https://t.me/BotFather)
- دسترسی به اینترنت از سرور

---

## 📄 مجوز

این پروژه متن‌باز است. برای اطلاعات بیشتر فایل [LICENSE](LICENSE) رو ببین.

---

<p align="center">ساخته‌شده با ❤️ توسط <a href="https://github.com/saeedpayab">saeedpayab</a></p>

</div>
`;

  function copyMD() {
    const activeTab = document.querySelector('.tab-content.active');
    const isFa = activeTab.id === 'tab-fa';
    const md = isFa ? MD_FA : MD_EN;
    navigator.clipboard.writeText(md).then(() => {
      const btn = document.getElementById('copyBtn');
      const prev = btn.innerHTML;
      btn.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Copied!`;
      btn.classList.add('copied');
      setTimeout(() => { btn.innerHTML = prev; btn.classList.remove('copied'); }, 2000);
    });
  }
</script>
</body>
</html>
