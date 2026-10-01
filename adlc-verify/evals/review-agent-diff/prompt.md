---
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill]
tags: [smoke, trigger, agent-code-review]
description: Should invoke agent-code-review and apply its method
---

Claude Code opened a PR that adds rate limiting to our public API. CI is green. Here is the spec and the diff. Review it before I approve.

SPEC (specs/rate-limit/spec.md)
- Limit each API key to 100 requests per minute on all /v1/* public endpoints.
- Return HTTP 429 with a Retry-After header when the limit is exceeded.
- Must work correctly with our 6 API instances behind the load balancer (shared state in Redis).
- Non-goal: no changes to authentication.

DIFF
--- a/src/middleware/rateLimit.ts
+++ b/src/middleware/rateLimit.ts
@@ +1,24 @@
+const hits = new Map<string, { count: number; windowStart: number }>();
+
+export function rateLimit(req, res, next) {
+  try {
+    const key = req.headers['x-forwarded-for'] || req.ip;
+    const now = Date.now();
+    const entry = hits.get(key) ?? { count: 0, windowStart: now };
+    if (now - entry.windowStart > 60_000) { entry.count = 0; entry.windowStart = now; }
+    entry.count += 1;
+    hits.set(key, entry);
+    res.setRateLimitHeaders({ limit: 100, remaining: Math.max(0, 100 - entry.count) });
+    if (entry.count > 100) {
+      return res.status(429).set('Retry-After', '60').send('Too Many Requests');
+    }
+    next();
+  } catch (e) {
+    next();
+  }
+}
--- a/src/middleware/auth.ts
+++ b/src/middleware/auth.ts
@@ -40,7 +40,6 @@ export function verifyToken(token) {
   const payload = jwt.decode(token);
-  if (payload.exp * 1000 < Date.now()) throw new AuthError('token expired');
   return payload;
 }
--- a/test/rateLimit.test.ts
+++ b/test/rateLimit.test.ts
@@ -18,7 +18,7 @@ it('blocks the 101st request in a minute', async () => {
   for (let i = 0; i < 100; i++) await request(app).get('/v1/items').set('x-api-key', 'k1');
   const res = await request(app).get('/v1/items').set('x-api-key', 'k1');
-  expect(res.status).toBe(429);
+  expect([200, 429]).toContain(res.status);
 });
