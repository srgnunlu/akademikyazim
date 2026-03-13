"use client";

import { useTranslations, useLocale } from "next-intl";
import { useRouter, usePathname } from "@/i18n/navigation";
import { routing } from "@/i18n/routing";
import { useState } from "react";
import { Menu, X } from "lucide-react";
import { trackEvent } from "@/lib/analytics";

const LOCALE_LABELS: Record<string, string> = {
  tr: "TR",
  en: "EN",
};

export default function Navigation() {
  const t = useTranslations("nav");
  const locale = useLocale();
  const router = useRouter();
  const pathname = usePathname();
  const [open, setOpen] = useState(false);

  const otherLocales = routing.locales.filter((l) => l !== locale);

  function switchLocale(target: string) {
    trackEvent("switch_language", { from: locale, to: target });
    router.replace(pathname, { locale: target });
  }

  const links = [
    { href: "#features", label: t("features") },
    { href: "#how-it-works", label: t("howItWorks") },
    { href: "#iron-rules", label: t("ironRules") },
    { href: "#doc-types", label: t("docTypes") },
    { href: "#architecture", label: t("techStack") },
    { href: "#roadmap", label: t("roadmap") },
    { href: "#faq", label: t("faq") },
  ];

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-background/80 backdrop-blur-md border-b border-border">
      <div className="max-w-6xl mx-auto px-6 h-14 flex items-center justify-between">
        <a
          href="#"
          className="text-sm font-bold tracking-tight text-foreground"
        >
          TezAtlas
        </a>

        <div className="hidden lg:flex items-center gap-6">
          {links.map((l) => (
            <a
              key={l.href}
              href={l.href}
              className="text-xs text-muted hover:text-foreground transition-colors"
            >
              {l.label}
            </a>
          ))}
          <a
            href="https://github.com/baristiran/tezatlas"
            target="_blank"
            rel="noopener noreferrer"
            className="text-xs text-muted hover:text-foreground transition-colors"
            onClick={() => trackEvent("click_github", { location: "nav" })}
          >
            {t("github")}
          </a>
          {otherLocales.map((target) => (
            <button
              key={target}
              onClick={() => switchLocale(target)}
              className="text-xs text-muted hover:text-foreground transition-colors border border-border rounded px-2 py-1"
              aria-label={`Switch to ${target}`}
            >
              {LOCALE_LABELS[target] ?? target.toUpperCase()}
            </button>
          ))}
        </div>

        <button
          className="lg:hidden text-foreground"
          onClick={() => setOpen(!open)}
          aria-label="Toggle menu"
        >
          {open ? <X size={18} /> : <Menu size={18} />}
        </button>
      </div>

      {open && (
        <div className="lg:hidden border-t border-border bg-background px-6 py-4 space-y-3">
          {links.map((l) => (
            <a
              key={l.href}
              href={l.href}
              onClick={() => setOpen(false)}
              className="block text-sm text-muted hover:text-foreground transition-colors"
            >
              {l.label}
            </a>
          ))}
          <a
            href="https://github.com/baristiran/tezatlas"
            target="_blank"
            rel="noopener noreferrer"
            className="block text-sm text-muted hover:text-foreground transition-colors"
          >
            {t("github")}
          </a>
          {otherLocales.map((target) => (
            <button
              key={target}
              onClick={() => {
                switchLocale(target);
                setOpen(false);
              }}
              className="text-sm text-muted hover:text-foreground transition-colors"
            >
              {LOCALE_LABELS[target] ?? target.toUpperCase()}
            </button>
          ))}
        </div>
      )}
    </nav>
  );
}
