import { useTranslations } from "next-intl";
import { Quote } from "lucide-react";

export default function Testimonials() {
  const t = useTranslations("testimonials");

  const items = Array.from({ length: 3 }, (_, i) => ({
    quote: t(`t${i + 1}quote`),
    name: t(`t${i + 1}name`),
    role: t(`t${i + 1}role`),
  }));

  return (
    <section id="testimonials" className="py-24 sm:py-32 px-6">
      <div className="max-w-5xl mx-auto">
        <span className="text-xs tracking-[0.2em] uppercase text-muted font-mono">
          {t("badge")}
        </span>
        <h2 className="text-3xl sm:text-4xl font-bold tracking-tight mt-3 mb-14">
          {t("title")}
        </h2>

        <div className="grid md:grid-cols-3 gap-6">
          {items.map((item, i) => (
            <div
              key={i}
              className="border border-border bg-surface p-6 flex flex-col"
            >
              <Quote size={16} className="text-muted mb-4" aria-hidden="true" />
              <blockquote className="text-sm leading-relaxed flex-1 mb-4">
                {item.quote}
              </blockquote>
              <div className="border-t border-border pt-4">
                <div className="text-sm font-bold">{item.name}</div>
                <div className="text-xs text-muted">{item.role}</div>
              </div>
            </div>
          ))}
        </div>

        <p className="text-xs text-muted mt-6 text-center">{t("note")}</p>
      </div>
    </section>
  );
}
