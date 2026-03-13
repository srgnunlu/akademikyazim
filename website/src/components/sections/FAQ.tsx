"use client";

import { useTranslations } from "next-intl";
import { useState } from "react";
import { ChevronDown } from "lucide-react";
import { trackEvent } from "@/lib/analytics";

export default function FAQ() {
  const t = useTranslations("faq");

  const items = Array.from({ length: 6 }, (_, i) => ({
    q: t(`q${i + 1}`),
    a: t(`a${i + 1}`),
  }));

  const [open, setOpen] = useState<number | null>(null);

  function toggle(i: number) {
    const next = open === i ? null : i;
    setOpen(next);
    if (next !== null) {
      trackEvent("open_faq", { question: i + 1 });
    }
  }

  return (
    <section id="faq" className="py-24 sm:py-32 px-6">
      <div className="max-w-3xl mx-auto">
        <span className="text-xs tracking-[0.2em] uppercase text-muted font-mono">
          {t("badge")}
        </span>
        <h2 className="text-3xl sm:text-4xl font-bold tracking-tight mt-3 mb-14">
          {t("title")}
        </h2>

        <div
          className="border border-border divide-y divide-border bg-surface"
          role="list"
        >
          {items.map((item, i) => {
            const isOpen = open === i;
            const panelId = `faq-panel-${i}`;
            const triggerId = `faq-trigger-${i}`;

            return (
              <div key={i} role="listitem">
                <button
                  id={triggerId}
                  onClick={() => toggle(i)}
                  aria-expanded={isOpen}
                  aria-controls={panelId}
                  className="w-full flex items-center justify-between p-5 text-left hover:bg-surface-alt transition-colors"
                >
                  <span className="text-sm font-medium pr-4">{item.q}</span>
                  <ChevronDown
                    size={16}
                    className={`text-muted shrink-0 transition-transform ${
                      isOpen ? "rotate-180" : ""
                    }`}
                    aria-hidden="true"
                  />
                </button>
                <div
                  id={panelId}
                  role="region"
                  aria-labelledby={triggerId}
                  hidden={!isOpen}
                  className={isOpen ? "px-5 pb-5" : ""}
                >
                  {isOpen && (
                    <p className="text-sm text-muted leading-relaxed">
                      {item.a}
                    </p>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
