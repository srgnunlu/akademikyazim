import createMiddleware from "next-intl/middleware";
import { routing } from "./i18n/routing";

export function proxy(request: Parameters<ReturnType<typeof createMiddleware>>[0]) {
  return createMiddleware(routing)(request);
}

export const config = {
  matcher: ["/", "/(tr|en)/:path*"],
};
