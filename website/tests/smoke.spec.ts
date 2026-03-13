import { test, expect } from "@playwright/test";

test.describe("Landing page smoke tests", () => {
  test("TR homepage loads with correct title", async ({ page }) => {
    await page.goto("/tr");
    await expect(page).toHaveTitle(/TezAtlas/);
    await expect(page.locator("h1")).toBeVisible();
  });

  test("EN homepage loads with correct title", async ({ page }) => {
    await page.goto("/en");
    await expect(page).toHaveTitle(/TezAtlas/);
    await expect(page.locator("h1")).toBeVisible();
  });

  test("navigation links are visible on desktop", async ({ page }) => {
    await page.goto("/tr");
    await page.setViewportSize({ width: 1280, height: 720 });
    await expect(page.locator('nav a[href="#features"]')).toBeVisible();
    await expect(page.locator('nav a[href="#faq"]')).toBeVisible();
  });

  test("language switcher works", async ({ page }) => {
    await page.goto("/tr");
    await page.setViewportSize({ width: 1280, height: 720 });
    const switcher = page.locator("nav button", { hasText: "EN" });
    await expect(switcher).toBeVisible();
    await switcher.click();
    await expect(page).toHaveURL(/\/en/);
  });

  test("FAQ accordion opens and closes", async ({ page }) => {
    await page.goto("/tr");
    const trigger = page.locator("#faq-trigger-0");
    await trigger.scrollIntoViewIfNeeded();
    await expect(trigger).toHaveAttribute("aria-expanded", "false");
    await trigger.click();
    await expect(trigger).toHaveAttribute("aria-expanded", "true");
    const panel = page.locator("#faq-panel-0");
    await expect(panel).toBeVisible();
    await trigger.click();
    await expect(trigger).toHaveAttribute("aria-expanded", "false");
  });

  test("CTA section has GitHub link and waitlist form", async ({ page }) => {
    await page.goto("/tr");
    const cta = page.locator("#cta");
    await cta.scrollIntoViewIfNeeded();
    await expect(
      cta.locator('a[href="https://github.com/baristiran/tezatlas"]')
    ).toBeVisible();
    await expect(cta.locator('input[type="email"]')).toBeVisible();
  });

  test("all major sections are present", async ({ page }) => {
    await page.goto("/tr");
    const ids = [
      "features",
      "how-it-works",
      "iron-rules",
      "doc-types",
      "architecture",
      "testimonials",
      "roadmap",
      "faq",
      "cta",
    ];
    for (const id of ids) {
      await expect(page.locator(`#${id}`)).toBeAttached();
    }
  });

  test("no console errors on page load", async ({ page }) => {
    const errors: string[] = [];
    page.on("console", (msg) => {
      if (msg.type() === "error") errors.push(msg.text());
    });
    await page.goto("/tr");
    await page.waitForLoadState("networkidle");
    expect(errors).toEqual([]);
  });

  test("JSON-LD FAQ schema is present", async ({ page }) => {
    await page.goto("/tr");
    const jsonLd = page.locator('script[type="application/ld+json"]');
    await expect(jsonLd).toBeAttached();
    const content = await jsonLd.textContent();
    expect(content).toContain("FAQPage");
  });
});
