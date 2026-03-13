import { useTranslations } from "next-intl";
import {
  Network,
  GitFork,
  Wrench,
  FileCode,
  BookOpen,
  Cog,
} from "lucide-react";

export default function TechStack() {
  const t = useTranslations("techStack");

  const stats = [
    { icon: Network, num: "~130", label: t("nodes") },
    { icon: GitFork, num: "10", label: t("phases") },
    { icon: Wrench, num: "30", label: t("techniques") },
    { icon: FileCode, num: "13", label: t("templates") },
    { icon: BookOpen, num: "5", label: t("disciplines") },
    { icon: Cog, num: "9", label: t("tools") },
  ];

  return (
    <section id="architecture" className="py-24 sm:py-32 px-6">
      <div className="max-w-5xl mx-auto">
        <span className="text-xs tracking-[0.2em] uppercase text-muted font-mono">
          {t("badge")}
        </span>
        <h2 className="text-3xl sm:text-4xl font-bold tracking-tight mt-3 mb-3">
          {t("title")}
        </h2>
        <p className="text-muted text-base max-w-2xl mb-14">{t("subtitle")}</p>

        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4 mb-12">
          {stats.map((s, i) => (
            <div
              key={i}
              className="border border-border bg-surface p-5 text-center"
            >
              <s.icon size={18} className="mx-auto text-muted mb-2" />
              <div className="text-2xl font-bold mb-1">{s.num}</div>
              <div className="text-xs text-muted">{s.label}</div>
            </div>
          ))}
        </div>

        <p className="text-sm text-muted leading-relaxed mb-8 max-w-3xl">
          {t("detail")}
        </p>

        <div className="bg-foreground text-background p-6 font-mono text-xs leading-loose">
          <div className="text-accent-muted mb-2">{t("providers")}</div>
          <div className="flex flex-wrap gap-3">
            {[
              "Gemini",
              "DeepSeek",
              "OpenAI",
              "Grok",
              "Groq",
              "Ollama",
              "Anthropic",
            ].map((p) => (
              <span
                key={p}
                className="border border-white/20 px-2 py-0.5 text-white/80"
              >
                {p}
              </span>
            ))}
          </div>
          <p className="text-white/50 mt-3 text-xs">{t("providersDetail")}</p>
        </div>
      </div>
    </section>
  );
}
