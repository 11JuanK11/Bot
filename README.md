# Travel Automation Bot

This project is an automated web bot developed using Selenium in Python. The bot interacts with the **Viajes Éxito** website to perform various actions such as searching for flight and hotel packages, selecting travel options, and retrieving package prices. It also demonstrates how to handle pop-ups, navigate through the site, and utilize advanced search features.

## Features

1. **Pop-Up Handling**:
   - Automatically detects and closes pop-ups on the website using `iframe` switching.

2. **Flight + Hotel Search**:
   - Selects the "Flight + Hotel" option on the website.
   - Inputs departure airport as José María Cordova and destination airport as Cancún, Quintana Roo.
   - Selects travel dates: Departure on 20-12-2024 and return on 4-1-2025.

3. **Room Selection**:
   - Adds multiple rooms and specifies the number of adults per room.

4. **Package Price Retrieval**:
   - Scrapes and prints prices of available travel packages in the console.

5. **Advanced Search**:
   - Searches for specific airlines (e.g., Avianca) using the advanced search functionality.

6. **Contact Us Section**:
   - Navigates to the "Contact Us" section and clicks the WhatsApp contact link.

7. **Dynamic Website Interaction**:
   - Handles scrolling, switching between tabs, and interacting with dynamically loaded content.

## Prerequisites

1. **Software Requirements**:
   - Python 3.13
   - Google Chrome browser 131.0.6778.140
   - ChromeDriver corresponding to this Chrome version

2. **Python Libraries**:
   - `selenium`

   Install the required library with:
   ```bash
   pip install selenium

---

## Creado por Juan Camilo Alzate
[GitHub Juan Camilo Alzate](https://github.com/11JuanK11)

---

## Creado por Sara Carolina Sánchez
[GitHub Sara Carolina Sánchez](https://github.com/Caro-26S)

---
