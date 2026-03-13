import { useTranslations } from "next-intl";

export default function Roadmap() {
  const t = useTranslations("roadmap");

  const phases = [
    {
      title: t("phase1title"),
      status: t("phase1status"),
      desc: t("phase1desc"),
      active: true,
    },
    {
      title: t("phase2title"),
      status: t("phase2status"),
      desc: t("phase2desc"),
      active: true,
    },
    {
      title: t("phase3title"),
      status: t("phase3status"),
      desc: t("phase3desc"),
      active: false,
    },
    {
      title: t("phase4title"),
      status: t("phase4status"),
      desc: t("phase4desc"),
      active: false,
    },
  ];

  return (
    <section id="roadmap" className="py-24 sm:py-32 px-6 bg-surface-alt">
      <div className="max-w-5xl mx-auto">
        <span className="text-xs tracking-[0.2em] uppercase text-muted font-mono">
          {t("badge")}
        </span>
        <h2 className="text-3xl sm:text-4xl font-bold tracking-tight mt-3 mb-3">
          {t("title")}
        </h2>
        <p className="text-muted text-base max-w-2xl mb-14">{t("subtitle")}</p>

        <div className="space-y-0 border border-border divide-y divide-border bg-surface">
          {phases.map((p, i) => (
            <div key={i} className="flex gap-6 p-6">
              <div className="shrink-0 flex flex-col items-center">
                <div
                  className={`w-3 h-3 rounded-full border-2 ${
                    p.active
                      ? "border-foreground bg-foreground"
                      : "border-border bg-transparent"
                  }`}
                />
                {i < phases.length - 1 && (
                  <div className="w-px flex-1 bg-border mt-1" />
                )}
              </div>
              <div>
                <div className="flex items-baseline gap-3 mb-1">
                  <h3 className="text-sm font-bold">{p.title}</h3>
                  <span
                    className={`text-xs font-mono ${
                      p.active ? "text-foreground" : "text-muted"
                    }`}
                  >
                    {p.status}
                  </span>
                </div>
                <p className="text-xs text-muted leading-relaxed">{p.desc}</p>
              </div>
            </div>
          ))}
        </div>

        <div className="mt-8 border-l-2 border-foreground pl-6">
          <p className="text-sm text-muted leading-relaxed">{t("byok")}</p>
        </div>
      </div>
    </section>
  );
}
