type EventName =
  | "click_github"
  | "click_docs"
  | "submit_waitlist"
  | "switch_language"
  | "view_section"
  | "open_faq";

type EventProps = Record<string, string | number | boolean>;

export function trackEvent(name: EventName, props?: EventProps) {
  if (typeof window === "undefined") return;

  // Google Analytics 4
  if (typeof window.gtag === "function") {
    window.gtag("event", name, props);
  }

  // Plausible
  if (typeof window.plausible === "function") {
    window.plausible(name, { props });
  }

  if (process.env.NODE_ENV === "development") {
    console.debug("[analytics]", name, props);
  }
}

declare global {
  interface Window {
    gtag?: (...args: unknown[]) => void;
    plausible?: (event: string, options?: { props?: EventProps }) => void;
  }
}
