import { useTranslations } from "next-intl";
import {
  Lock,
  Shield,
  AlignLeft,
  Mic,
  Users,
  ScanLine,
  Tag,
  Swords,
  Brain,
  BookOpen,
  Puzzle,
  RefreshCw,
} from "lucide-react";

export default function Features() {
  const t = useTranslations("features");

  const features = [
    { icon: Lock, title: t("f1title"), desc: t("f1") },
    { icon: Shield, title: t("f2title"), desc: t("f2") },
    { icon: AlignLeft, title: t("f3title"), desc: t("f3") },
    { icon: Mic, title: t("f4title"), desc: t("f4") },
    { icon: Users, title: t("f5title"), desc: t("f5") },
    { icon: ScanLine, title: t("f6title"), desc: t("f6") },
    { icon: Tag, title: t("f7title"), desc: t("f7") },
    { icon: Swords, title: t("f8title"), desc: t("f8") },
    { icon: Brain, title: t("f9title"), desc: t("f9") },
    { icon: BookOpen, title: t("f10title"), desc: t("f10") },
    { icon: Puzzle, title: t("f11title"), desc: t("f11") },
    { icon: RefreshCw, title: t("f12title"), desc: t("f12") },
  ];

  return (
    <section id="features" className="py-24 sm:py-32 px-6 bg-surface-alt">
      <div className="max-w-5xl mx-auto">
        <span className="text-xs tracking-[0.2em] uppercase text-muted font-mono">
          {t("badge")}
        </span>
        <h2 className="text-3xl sm:text-4xl font-bold tracking-tight mt-3 mb-3">
          {t("title")}
        </h2>
        <p className="text-muted text-base max-w-2xl mb-14">{t("subtitle")}</p>

        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {features.map((f, i) => (
            <div
              key={i}
              className="border border-border bg-surface p-6 hover:border-foreground/20 transition-colors"
            >
              <f.icon size={18} className="text-muted mb-3" />
              <h3 className="text-sm font-bold mb-2">{f.title}</h3>
              <p className="text-xs text-muted leading-relaxed">{f.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
