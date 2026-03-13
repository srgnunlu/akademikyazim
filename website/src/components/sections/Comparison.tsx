import { useTranslations } from "next-intl";
import { Check, X, Minus } from "lucide-react";

export default function Comparison() {
  const t = useTranslations("comparison");

  type Val = "yes" | "no" | "partial";

  const rows: { key: string; ta: Val; cg: Val; gr: Val; me: Val }[] = [
    { key: "f1", ta: "yes", cg: "no", gr: "no", me: "partial" },
    { key: "f2", ta: "yes", cg: "no", gr: "no", me: "no" },
    { key: "f3", ta: "yes", cg: "no", gr: "no", me: "no" },
    { key: "f4", ta: "yes", cg: "no", gr: "no", me: "no" },
    { key: "f5", ta: "yes", cg: "no", gr: "no", me: "no" },
    { key: "f6", ta: "yes", cg: "no", gr: "no", me: "no" },
    { key: "f7", ta: "yes", cg: "no", gr: "no", me: "no" },
    { key: "f8", ta: "yes", cg: "no", gr: "no", me: "no" },
    { key: "f9", ta: "yes", cg: "no", gr: "partial", me: "no" },
    { key: "f10", ta: "yes", cg: "no", gr: "no", me: "no" },
  ];

  function Icon({ val }: { val: Val }) {
    if (val === "yes")
      return <Check size={14} className="text-foreground mx-auto" />;
    if (val === "partial")
      return <Minus size={14} className="text-muted mx-auto" />;
    return <X size={14} className="text-muted/40 mx-auto" />;
  }

  return (
    <section className="py-24 sm:py-32 px-6">
      <div className="max-w-5xl mx-auto">
        <span className="text-xs tracking-[0.2em] uppercase text-muted font-mono">
          {t("badge")}
        </span>
        <h2 className="text-3xl sm:text-4xl font-bold tracking-tight mt-3 mb-14">
          {t("title")}
        </h2>

        <div className="overflow-x-auto">
          <table className="w-full text-xs border border-border">
            <thead>
              <tr className="bg-surface-alt">
                <th className="text-left p-3 font-medium text-muted border-b border-border">
                  {t("feature")}
                </th>
                <th className="p-3 font-bold border-b border-border text-center">
                  {t("tezatlas")}
                </th>
                <th className="p-3 font-medium text-muted border-b border-border text-center">
                  {t("chatgpt")}
                </th>
                <th className="p-3 font-medium text-muted border-b border-border text-center">
                  {t("grammarly")}
                </th>
                <th className="p-3 font-medium text-muted border-b border-border text-center">
                  {t("mendeley")}
                </th>
              </tr>
            </thead>
            <tbody>
              {rows.map((r) => (
                <tr key={r.key} className="border-b border-border last:border-0">
                  <td className="p-3 text-muted">{t(r.key)}</td>
                  <td className="p-3">
                    <Icon val={r.ta} />
                  </td>
                  <td className="p-3">
                    <Icon val={r.cg} />
                  </td>
                  <td className="p-3">
                    <Icon val={r.gr} />
                  </td>
                  <td className="p-3">
                    <Icon val={r.me} />
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </section>
  );
}
