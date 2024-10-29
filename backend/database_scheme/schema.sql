-- schema.sql

-- Destinations table
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

CREATE SEQUENCE public.destinations_destination_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.destinations_destination_id_seq OWNER TO fizzdeen;

ALTER SEQUENCE public.destinations_destination_id_seq OWNED BY public.destinations.destination_id;

ALTER TABLE ONLY public.destinations ALTER COLUMN destination_id SET DEFAULT nextval('public.destinations_destination_id_seq'::regclass);


-- Itineraries table
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

CREATE SEQUENCE public.itineraries_itinerary_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.itineraries_itinerary_id_seq OWNER TO fizzdeen;

ALTER SEQUENCE public.itineraries_itinerary_id_seq OWNED BY public.itineraries.itinerary_id;

ALTER TABLE ONLY public.itineraries ALTER COLUMN itinerary_id SET DEFAULT nextval('public.itineraries_itinerary_id_seq'::regclass);


-- Payments table
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

CREATE SEQUENCE public.payments_payment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.payments_payment_id_seq OWNER TO   
 fizzdeen;

ALTER SEQUENCE public.payments_payment_id_seq OWNED BY public.payments.payment_id;

ALTER TABLE ONLY public.payments ALTER COLUMN payment_id SET DEFAULT nextval('public.payments_payment_id_seq'::regclass);


-- Users table
CREATE TABLE public.users (
    users_id integer NOT NULL,
    username character varying(50) NOT NULL,
    email character varying(100) NOT NULL,
    password character varying(255)   
 NOT NULL,
    first_name character varying(50),
    last_name character varying(50),
    phone_no character varying(20),
    date_of_birth date,
    city character varying(50),
    country character varying(50),
    subscription_type character varying(20)
);

ALTER TABLE public.users OWNER TO fizzdeen;

CREATE SEQUENCE public.users_users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.users_users_id_seq OWNER TO   
 fizzdeen;

ALTER SEQUENCE public.users_users_id_seq OWNED BY public.users.users_id;

ALTER TABLE ONLY public.users ALTER COLUMN users_id SET DEFAULT nextval('public.users_users_id_seq'::regclass);