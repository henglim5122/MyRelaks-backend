--
-- PostgreSQL database dump
--

-- Dumped from database version 14.13 (Homebrew)
-- Dumped by pg_dump version 14.13 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: destinations; Type: TABLE; Schema: public; Owner: fizzdeen
--

CREATE TABLE public.destinations (
    destination_id integer NOT NULL,
    name character varying(100) NOT NULL,
    location character varying(100),
    state character varying(50),
    description text,
    coordinates point,
    ratings_review text,
    price numeric(10,2),
    liked_by integer[]
);


ALTER TABLE public.destinations OWNER TO fizzdeen;

--
-- Name: destinations_destination_id_seq; Type: SEQUENCE; Schema: public; Owner: fizzdeen
--

CREATE SEQUENCE public.destinations_destination_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.destinations_destination_id_seq OWNER TO fizzdeen;

--
-- Name: destinations_destination_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: fizzdeen
--

ALTER SEQUENCE public.destinations_destination_id_seq OWNED BY public.destinations.destination_id;


--
-- Name: itineraries; Type: TABLE; Schema: public; Owner: fizzdeen
--

CREATE TABLE public.itineraries (
    itinerary_id integer NOT NULL,
    trip_name character varying(100) NOT NULL,
    trip_dates daterange,
    activities text,
    total_budget numeric(10,2),
    estimated_cost numeric(10,2),
    users_id integer,
    destination_id integer
);


ALTER TABLE public.itineraries OWNER TO fizzdeen;

--
-- Name: itineraries_itinerary_id_seq; Type: SEQUENCE; Schema: public; Owner: fizzdeen
--

CREATE SEQUENCE public.itineraries_itinerary_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.itineraries_itinerary_id_seq OWNER TO fizzdeen;

--
-- Name: itineraries_itinerary_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: fizzdeen
--

ALTER SEQUENCE public.itineraries_itinerary_id_seq OWNED BY public.itineraries.itinerary_id;


--
-- Name: payments; Type: TABLE; Schema: public; Owner: fizzdeen
--

CREATE TABLE public.payments (
    payment_id integer NOT NULL,
    amount numeric(10,2) NOT NULL,
    payment_method character varying(50),
    payment_status character varying(20),
    payment_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    encrypted_payment_info text,
    users_id integer
);


ALTER TABLE public.payments OWNER TO fizzdeen;

--
-- Name: payments_payment_id_seq; Type: SEQUENCE; Schema: public; Owner: fizzdeen
--

CREATE SEQUENCE public.payments_payment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.payments_payment_id_seq OWNER TO fizzdeen;

--
-- Name: payments_payment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: fizzdeen
--

ALTER SEQUENCE public.payments_payment_id_seq OWNED BY public.payments.payment_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: fizzdeen
--

CREATE TABLE public.users (
    users_id integer NOT NULL,
    username character varying(50) NOT NULL,
    email character varying(100) NOT NULL,
    password character varying(255) NOT NULL,
    first_name character varying(50),
    last_name character varying(50),
    phone_no character varying(20),
    date_of_birth date,
    city character varying(50),
    country character varying(50),
    subscription_type character varying(20)
);


ALTER TABLE public.users OWNER TO fizzdeen;

--
-- Name: users_users_id_seq; Type: SEQUENCE; Schema: public; Owner: fizzdeen
--

CREATE SEQUENCE public.users_users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_users_id_seq OWNER TO fizzdeen;

--
-- Name: users_users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: fizzdeen
--

ALTER SEQUENCE public.users_users_id_seq OWNED BY public.users.users_id;


--
-- Name: destinations destination_id; Type: DEFAULT; Schema: public; Owner: fizzdeen
--

ALTER TABLE ONLY public.destinations ALTER COLUMN destination_id SET DEFAULT nextval('public.destinations_destination_id_seq'::regclass);


--
-- Name: itineraries itinerary_id; Type: DEFAULT; Schema: public; Owner: fizzdeen
--

ALTER TABLE ONLY public.itineraries ALTER COLUMN itinerary_id SET DEFAULT nextval('public.itineraries_itinerary_id_seq'::regclass);


--
-- Name: payments payment_id; Type: DEFAULT; Schema: public; Owner: fizzdeen
--

ALTER TABLE ONLY public.payments ALTER COLUMN payment_id SET DEFAULT nextval('public.payments_payment_id_seq'::regclass);


--
-- Name: users users_id; Type: DEFAULT; Schema: public; Owner: fizzdeen
--

ALTER TABLE ONLY public.users ALTER COLUMN users_id SET DEFAULT nextval('public.users_users_id_seq'::regclass);


--
-- Data for Name: destinations; Type: TABLE DATA; Schema: public; Owner: fizzdeen
--

COPY public.destinations (destination_id, name, location, state, description, coordinates, ratings_review, price, liked_by) FROM stdin;
\.


--
-- Data for Name: itineraries; Type: TABLE DATA; Schema: public; Owner: fizzdeen
--

COPY public.itineraries (itinerary_id, trip_name, trip_dates, activities, total_budget, estimated_cost, users_id, destination_id) FROM stdin;
\.


--
-- Data for Name: payments; Type: TABLE DATA; Schema: public; Owner: fizzdeen
--

COPY public.payments (payment_id, amount, payment_method, payment_status, payment_date, encrypted_payment_info, users_id) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: fizzdeen
--

COPY public.users (users_id, username, email, password, first_name, last_name, phone_no, date_of_birth, city, country, subscription_type) FROM stdin;
\.


--
-- Name: destinations_destination_id_seq; Type: SEQUENCE SET; Schema: public; Owner: fizzdeen
--

SELECT pg_catalog.setval('public.destinations_destination_id_seq', 1, false);


--
-- Name: itineraries_itinerary_id_seq; Type: SEQUENCE SET; Schema: public; Owner: fizzdeen
--

SELECT pg_catalog.setval('public.itineraries_itinerary_id_seq', 1, false);


--
-- Name: payments_payment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: fizzdeen
--

SELECT pg_catalog.setval('public.payments_payment_id_seq', 1, false);


--
-- Name: users_users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: fizzdeen
--

SELECT pg_catalog.setval('public.users_users_id_seq', 1, false);


--
-- Name: destinations destinations_pkey; Type: CONSTRAINT; Schema: public; Owner: fizzdeen
--

ALTER TABLE ONLY public.destinations
    ADD CONSTRAINT destinations_pkey PRIMARY KEY (destination_id);


--
-- Name: itineraries itineraries_pkey; Type: CONSTRAINT; Schema: public; Owner: fizzdeen
--

ALTER TABLE ONLY public.itineraries
    ADD CONSTRAINT itineraries_pkey PRIMARY KEY (itinerary_id);


--
-- Name: payments payments_pkey; Type: CONSTRAINT; Schema: public; Owner: fizzdeen
--

ALTER TABLE ONLY public.payments
    ADD CONSTRAINT payments_pkey PRIMARY KEY (payment_id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: fizzdeen
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: fizzdeen
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (users_id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: fizzdeen
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: itineraries itineraries_destination_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: fizzdeen
--

ALTER TABLE ONLY public.itineraries
    ADD CONSTRAINT itineraries_destination_id_fkey FOREIGN KEY (destination_id) REFERENCES public.destinations(destination_id) ON DELETE CASCADE;


--
-- Name: itineraries itineraries_users_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: fizzdeen
--

ALTER TABLE ONLY public.itineraries
    ADD CONSTRAINT itineraries_users_id_fkey FOREIGN KEY (users_id) REFERENCES public.users(users_id) ON DELETE CASCADE;


--
-- Name: payments payments_users_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: fizzdeen
--

ALTER TABLE ONLY public.payments
    ADD CONSTRAINT payments_users_id_fkey FOREIGN KEY (users_id) REFERENCES public.users(users_id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

