import { useTranslations } from "next-intl";

export default function Research() {
  const t = useTranslations("research");

  const items = [
    {
      author: t("r1author"),
      finding: t("r1finding"),
      response: t("r1response"),
    },
    {
      author: t("r2author"),
      finding: t("r2finding"),
      response: t("r2response"),
    },
    {
      author: t("r3author"),
      finding: t("r3finding"),
      response: t("r3response"),
    },
    {
      author: t("r4author"),
      finding: t("r4finding"),
      response: t("r4response"),
    },
  ];

  return (
    <section className="py-24 sm:py-32 px-6 bg-surface-alt">
      <div className="max-w-5xl mx-auto">
        <span className="text-xs tracking-[0.2em] uppercase text-muted font-mono">
          {t("badge")}
        </span>
        <h2 className="text-3xl sm:text-4xl font-bold tracking-tight mt-3 mb-14">
          {t("title")}
        </h2>

        <div className="space-y-6">
          {items.map((r, i) => (
            <div key={i} className="border border-border bg-surface p-6">
              <div className="text-xs font-mono text-muted mb-2">
                {r.author}
              </div>
              <p className="text-sm mb-3 leading-relaxed">{r.finding}</p>
              <div className="text-xs text-muted border-t border-border pt-3">
                <span className="font-bold">TezAtlas →</span> {r.response}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
