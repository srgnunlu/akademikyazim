"use client";

import { useTranslations } from "next-intl";
import { Github, BookOpen, Mail, Check, Loader2 } from "lucide-react";
import { useState, type FormEvent } from "react";
import { trackEvent } from "@/lib/analytics";

export default function CTA() {
  const t = useTranslations("cta");
  const [email, setEmail] = useState("");
  const [status, setStatus] = useState<"idle" | "loading" | "success" | "error">("idle");

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    if (!email.trim()) return;

    setStatus("loading");
    trackEvent("submit_waitlist", { email_domain: email.split("@")[1] ?? "" });

    // Simulated — replace with actual API endpoint (ConvertKit, Mailchimp, Resend, etc.)
    await new Promise((r) => setTimeout(r, 800));
    setStatus("success");
    setEmail("");
  }

  return (
    <section id="cta" className="py-24 sm:py-32 px-6">
      <div className="max-w-3xl mx-auto text-center">
        <h2 className="text-3xl sm:text-4xl font-bold tracking-tight mb-4">
          {t("title")}
        </h2>
        <p className="text-muted text-base mb-10">{t("subtitle")}</p>

        <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-12">
          <a
            href="https://github.com/baristiran/tezatlas"
            target="_blank"
            rel="noopener noreferrer"
            onClick={() => trackEvent("click_github", { location: "cta" })}
            className="inline-flex items-center gap-2 bg-foreground text-background px-6 py-3 text-sm font-medium hover:bg-foreground/90 transition-colors"
          >
            <Github size={16} />
            {t("button")}
          </a>
          <a
            href="https://github.com/baristiran/tezatlas#1-what-is-tezatlas"
            target="_blank"
            rel="noopener noreferrer"
            onClick={() => trackEvent("click_docs", { location: "cta" })}
            className="inline-flex items-center gap-2 border border-border text-foreground px-6 py-3 text-sm font-medium hover:bg-surface-alt transition-colors"
          >
            <BookOpen size={16} />
            {t("secondary")}
          </a>
        </div>

        <div className="border border-border bg-surface p-8 max-w-md mx-auto">
          <div className="flex items-center gap-2 justify-center mb-3">
            <Mail size={16} className="text-muted" />
            <h3 className="text-sm font-bold">{t("waitlistTitle")}</h3>
          </div>
          <p className="text-xs text-muted mb-5">{t("waitlistDesc")}</p>

          {status === "success" ? (
            <div className="flex items-center justify-center gap-2 text-sm text-foreground py-3">
              <Check size={16} />
              {t("waitlistSuccess")}
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="flex gap-2">
              <input
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder={t("waitlistPlaceholder")}
                className="flex-1 border border-border bg-background px-3 py-2 text-sm font-mono placeholder:text-muted/50 focus:outline-none focus:border-foreground transition-colors"
              />
              <button
                type="submit"
                disabled={status === "loading"}
                className="bg-foreground text-background px-4 py-2 text-sm font-medium hover:bg-foreground/90 transition-colors disabled:opacity-50"
              >
                {status === "loading" ? (
                  <Loader2 size={16} className="animate-spin" />
                ) : (
                  t("waitlistButton")
                )}
              </button>
            </form>
          )}
        </div>
      </div>
    </section>
  );
}
