import { useTranslations } from "next-intl";
import { AlertTriangle, FileWarning, GitBranchPlus, Eye } from "lucide-react";

export default function Problem() {
  const t = useTranslations("problem");

  const points = [
    { icon: FileWarning, title: t("point1title"), desc: t("point1") },
    { icon: AlertTriangle, title: t("point2title"), desc: t("point2") },
    { icon: GitBranchPlus, title: t("point3title"), desc: t("point3") },
    { icon: Eye, title: t("point4title"), desc: t("point4") },
  ];

  return (
    <section className="py-24 sm:py-32 px-6">
      <div className="max-w-5xl mx-auto">
        <span className="text-xs tracking-[0.2em] uppercase text-muted font-mono">
          {t("badge")}
        </span>
        <h2 className="text-3xl sm:text-4xl font-bold tracking-tight mt-3 mb-4">
          {t("title")}
        </h2>
        <p className="text-muted text-base max-w-2xl mb-12">
          {t("description")}
        </p>

        <div className="grid sm:grid-cols-2 gap-6 mb-12">
          {points.map((p, i) => (
            <div
              key={i}
              className="border border-border p-6 bg-surface hover:bg-surface-alt transition-colors"
            >
              <p.icon size={18} className="text-muted mb-3" />
              <h3 className="text-sm font-bold mb-2">{p.title}</h3>
              <p className="text-sm text-muted leading-relaxed">{p.desc}</p>
            </div>
          ))}
        </div>

        <div className="border-l-2 border-foreground pl-6">
          <p className="text-sm leading-relaxed font-medium">{t("solution")}</p>
        </div>
      </div>
    </section>
  );
}
