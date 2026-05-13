from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # ── Login ──────────────────────────────────────────────────────────────
    page.goto("http://192.168.30.17")
    page.fill('input[type="text"]', "distributor")
    page.fill('input[type="password"]', "distributor")
    page.press('input[type="password"]', "Enter")
    page.wait_for_load_state('networkidle')

    # ── Navigate to Hardware Health ────────────────────────────────────────
    page.goto("http://192.168.30.17/monitoring/diagnostics")
    page.wait_for_load_state('networkidle')

    # Wait for the diagnostics table to actually render
    page.wait_for_selector("div.diagnostics_overview", timeout=10000)
    page.wait_for_timeout(2000)

    # ── Expand all collapsed sections (click all section headers) ──────────
    section_headers = page.locator("div.diagnostics_table ul > li > div.mainrow").all()
    for header in section_headers:
        try:
            header.click()
            page.wait_for_timeout(300)
        except:
            pass

    page.wait_for_timeout(1000)

    # ── Scrape all name/value pairs ────────────────────────────────────────
    results = {}
    current_section = "Unknown"

    # Each top-level li is a section (Bluetooth, Computer, Motors, etc.)
    sections = page.locator("div.diagnostics_table > ul > li").all()

    for section in sections:
        # Section name is in the mainrow div
        try:
            section_name = section.locator("div.mainrow div.name").first.inner_text().strip()
            current_section = section_name
            results[current_section] = {}
        except:
            continue

        # Sub-items are nested li elements
        sub_items = section.locator("ul > li").all()
        for item in sub_items:
            try:
                name  = item.locator("div.name").first.inner_text().strip()
                value = item.locator("div.valuerow").first.inner_text().strip()
                if name:
                    results[current_section][name] = value
            except:
                pass

    # ── Print results ──────────────────────────────────────────────────────
    for section, fields in results.items():
        print(f"\n── {section} ──")
        for k, v in fields.items():
            print(f"  {k:<25} {v}")

    # ── Pull specific values you care about ───────────────────────────────
    print("\n── Key Values ──────────────────────────────────────")
    print("Signal Level :", results.get("Computer", {}).get("Signal Level", "N/A"))
    #print("SSID         :", results.get("Computer", {}).get("SSID", "N/A"))
    #print("IP Address   :", results.get("Computer", {}).get("IP address", "N/A"))
    #print("CPU load     :", results.get("Computer", {}).get("CPU load", "N/A"))
    #print("CPU Temp     :", results.get("Computer", {}).get("CPU Temperature", "N/A"))

    # ── Save to JSON ───────────────────────────────────────────────────────
    with open("hardware_health.json", "w") as f:
        json.dump(results, f, indent=2)
    print("\nSaved to hardware_health.json")

    browser.close()