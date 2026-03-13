import { useTranslations } from "next-intl";

export default function Stats() {
  const t = useTranslations("stats");

  const items = [
    { value: "~130", label: t("nodes") },
    { value: "10", label: t("docTypes") },
    { value: "9", label: t("ironRules") },
    { value: "5", label: t("disciplines") },
    { value: "3", label: t("agents") },
    { value: "0", label: t("hallucinations") },
  ];

  return (
    <section className="py-16 px-6 bg-foreground text-background">
      <div className="max-w-5xl mx-auto">
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-8">
          {items.map((s, i) => (
            <div key={i} className="text-center">
              <div className="text-3xl sm:text-4xl font-bold mb-1 font-mono">
                {s.value}
              </div>
              <div className="text-xs text-white/60">{s.label}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
