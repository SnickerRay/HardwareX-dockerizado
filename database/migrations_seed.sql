--
-- PostgreSQL database dump
--

\restrict 1bU3DsfBKpab4YYjrbEvOhj66St1gbMfVeoEZYm3QWaZwWbuREDBFYkB80Oc8No

-- Dumped from database version 18.6
-- Dumped by pg_dump version 18.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2026-08-16 14:50:19.414308+00
2	auth	0001_initial	2026-08-16 14:50:19.478527+00
3	admin	0001_initial	2026-08-16 14:50:19.492282+00
4	admin	0002_logentry_remove_auto_add	2026-08-16 14:50:19.495793+00
5	admin	0003_logentry_add_action_flag_choices	2026-08-16 14:50:19.500301+00
6	contenttypes	0002_remove_content_type_name	2026-08-16 14:50:19.511524+00
7	auth	0002_alter_permission_name_max_length	2026-08-16 14:50:19.519566+00
8	auth	0003_alter_user_email_max_length	2026-08-16 14:50:19.524334+00
9	auth	0004_alter_user_username_opts	2026-08-16 14:50:19.528851+00
10	auth	0005_alter_user_last_login_null	2026-08-16 14:50:19.533636+00
11	auth	0006_require_contenttypes_0002	2026-08-16 14:50:19.534398+00
12	auth	0007_alter_validators_add_error_messages	2026-08-16 14:50:19.538109+00
13	auth	0008_alter_user_username_max_length	2026-08-16 14:50:19.546953+00
14	auth	0009_alter_user_last_name_max_length	2026-08-16 14:50:19.55239+00
15	auth	0010_alter_group_name_max_length	2026-08-16 14:50:19.558442+00
16	auth	0011_update_proxy_permissions	2026-08-16 14:50:19.563263+00
17	auth	0012_alter_user_first_name_max_length	2026-08-16 14:50:19.56876+00
18	sessions	0001_initial	2026-08-16 14:50:19.576178+00
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 18, true);


--
-- PostgreSQL database dump complete
--

\unrestrict 1bU3DsfBKpab4YYjrbEvOhj66St1gbMfVeoEZYm3QWaZwWbuREDBFYkB80Oc8No

