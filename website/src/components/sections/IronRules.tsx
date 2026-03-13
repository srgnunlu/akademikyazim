import { useTranslations } from "next-intl";

export default function IronRules() {
  const t = useTranslations("ironRules");

  const rules = Array.from({ length: 9 }, (_, i) => ({
    num: String(i + 1).padStart(2, "0"),
    title: t(`r${i + 1}title`),
    desc: t(`r${i + 1}`),
  }));

  return (
    <section id="iron-rules" className="py-24 sm:py-32 px-6 bg-surface-alt">
      <div className="max-w-5xl mx-auto">
        <span className="text-xs tracking-[0.2em] uppercase text-muted font-mono">
          {t("badge")}
        </span>
        <h2 className="text-3xl sm:text-4xl font-bold tracking-tight mt-3 mb-3">
          {t("title")}
        </h2>
        <p className="text-muted text-base max-w-2xl mb-14">{t("subtitle")}</p>

        <div className="space-y-0 border border-border divide-y divide-border bg-surface">
          {rules.map((r) => (
            <div key={r.num} className="flex gap-6 p-6">
              <span className="text-xs text-muted font-mono shrink-0 pt-0.5">
                {r.num}
              </span>
              <div>
                <h3 className="text-sm font-bold mb-1">{r.title}</h3>
                <p className="text-xs text-muted leading-relaxed">{r.desc}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
