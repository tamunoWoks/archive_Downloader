# XKCD Archive Downloader

### Overview:
that automatically downloads comics from the [xkcd.com](https://xkcd.com) website. Starting from the most recent comic, the script saves each comic image locally and then navigates backward using the "Previous" comic link. This process continues until either the first XKCD comic is reached or a predefined maximum download limit is met.

The script is designed to be:
- Safe and respectful to the XKCD servers
- Easy to read and modify
- Deterministic and bounded (no infinite crawling)

The project demonstrates practical web scraping concepts, including HTTP requests, HTML parsing, link traversal, and file handling. It is well-suited as a learning project for developers seeking hands-on experience with automation, iterative scraping, and respectful, rule-based content downloading.

### Features:
- Downloads XKCD comics sequentially (latest to older)
- Saves images to a local directory
- Enforces a maximum download limit
- Uses rate limiting to avoid server abuse
- Includes basic error handling via HTTP status checks
