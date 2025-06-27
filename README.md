# 🍅 Pomodoro Task & Time Tracker  
**Python + Streamlit productivity timer** implementing the Pomodoro Technique with modern enhancements including email notifications (Gmail supported), animated visual feedback, motivational quotes, and optional sound alerts using alarm.mp3.  

## Core Features  
• 25-minute focused work sessions  
• 5-minute short breaks (15-minute long breaks after 4 cycles)  
• Real-time countdown display with progress visualization  
• Email/SMS notifications when sessions complete  
• Dynamic motivational quotes  
• Optional audio cues (requires alarm.mp3 in root directory)  

# Pomodoro Tracker Setup Guide

## Installation Instructions

1. **Clone repository and install dependencies**  
   ```bash
   git clone https://github.com/amal-alexander/pomodoro-tracker && cd pomodoro-tracker && pip install -r requirements.txt
   ```

2. **Add optional alarm sound** *(skip if not needed)*  
   ```bash
   cp /path/to/your/alarm.mp3 .
   ```

4. **Launch application**  
   ```bash
   streamlit run main.py
   ```

## Important Notes
- Replace `your@gmail.com` and `your_app_password` with actual credentials
- For Gmail, use an [App Password](https://myaccount.google.com/apppasswords) if 2FA is enabled
- Alarm sound must be in MP3 format

## Additional Notes
- Ensure you have Python 3.7+ installed
- Requires `pip` for package management
- First run may take longer while models download
## Configuration Options  
• Adjust session lengths by editing WORK_DURATION/BREAK_DURATION in .env  
• Disable sounds with ENABLE_SOUND=false  
• Gmail requires 2FA and app password setup  
• Customize notifications via SMTP settings  

## Visual Preview  
[Pomodoro Timer Interface] - Shows circular countdown timer with percentage completion, current phase indicator (Work/Break), and motivational quote display area.  

## Screenshot

![image](https://github.com/user-attachments/assets/78d2944b-3859-4292-80cc-e2c808d3448e)


## 👨💻 Creator  
**Amal Alexander** - [GitHub Profile](https://github.com/amal-alexander)  

## 🤝 Contributing  
Pull requests welcome! Please open issues first to discuss proposed changes.  

## 📜 License  
MIT License  
Copyright (c) 2023 Amal Alexander  

Permission is hereby granted... [standard MIT license text]  
