# sdlc_pattern_detector
An AI-powered tool that analyzes project timelines to detect SDLC process breaks like skipped phases, delayed hand-offs, and untested deployments.

This tool analyzes project history (like Jira exports or timeline reports) to automatically:

Detect missing SDLC phases
Highlight out-of-order phase executions
Generate visual flow diagrams (Mermaid.js syntax)
Summarize key risks and insights

Tool/Technology
Data Handling | Python, Pandas
AI Logic | Rule-based engine, NLP-ready
Visualization | Mermaid.js (flow diagrams)
App Frontend | Streamlit
Optional Exports | Power BI, CSV, Markdown

Features
✅ Upload SDLC project timelines (CSV format)
✅ Auto-detect missing phases (e.g., skipped QA, missing UAT)
✅ Auto-detect phase order violations
✅ Generate easy-to-understand Mermaid flow diagrams
✅ Provide smart risk insights and alerts
