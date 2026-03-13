import { useTranslations } from "next-intl";
import {
  GraduationCap,
  FileText,
  Presentation,
  Library,
  ClipboardList,
  BookOpen,
  Banknote,
  FileSearch,
  Image,
  FlaskConical,
} from "lucide-react";

export default function DocTypes() {
  const t = useTranslations("docTypes");

  const types = [
    { icon: GraduationCap, key: "thesis" },
    { icon: FileText, key: "article" },
    { icon: Presentation, key: "conference" },
    { icon: Library, key: "litReview" },
    { icon: ClipboardList, key: "report" },
    { icon: BookOpen, key: "bookChapter" },
    { icon: Banknote, key: "grant" },
    { icon: FileSearch, key: "proposal" },
    { icon: Image, key: "poster" },
    { icon: FlaskConical, key: "technical" },
  ] as const;

  return (
    <section id="doc-types" className="py-24 sm:py-32 px-6">
      <div className="max-w-5xl mx-auto">
        <span className="text-xs tracking-[0.2em] uppercase text-muted font-mono">
          {t("badge")}
        </span>
        <h2 className="text-3xl sm:text-4xl font-bold tracking-tight mt-3 mb-3">
          {t("title")}
        </h2>
        <p className="text-muted text-base max-w-2xl mb-14">{t("subtitle")}</p>

        <div className="grid sm:grid-cols-2 gap-4">
          {types.map((dt) => (
            <div
              key={dt.key}
              className="flex items-start gap-4 border border-border p-5 bg-surface hover:bg-surface-alt transition-colors"
            >
              <dt.icon size={18} className="text-muted mt-0.5 shrink-0" />
              <div>
                <div className="flex items-baseline gap-2 mb-1">
                  <h3 className="text-sm font-bold">{t(dt.key)}</h3>
                  <span className="text-xs text-muted font-mono">
                    {t(`${dt.key}Phases`)}
                  </span>
                </div>
                <p className="text-xs text-muted leading-relaxed">
                  {t(`${dt.key}Desc`)}
                </p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
