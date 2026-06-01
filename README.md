# Chowlet

## Overview

Chowlet is a campus-first food delivery platform designed to eliminate long food queues in universities and tertiary institutions across Nigeria.

The platform enables students to browse menus from restaurants within their school, place orders from their mobile devices, and receive food deliveries at designated locations within the campus.

Unlike traditional food delivery platforms that operate city-wide, Chowlet focuses on intra-campus logistics, making food delivery faster, more predictable, and easier to manage.

The long-term vision is to become the operating system for campus food commerce across Nigerian universities.

---

# Problem Statement

Students often spend significant time waiting in queues at cafeterias and food vendors.

Common challenges include:

* Long waiting times during peak hours
* Missed lectures due to food queues
* Lack of visibility into restaurant availability
* Inefficient ordering process
* No centralized platform for campus food vendors

Chowlet solves these problems by allowing students to order ahead and receive food without physically joining a queue.

---

# Business Model

Chowlet generates revenue through a service fee added to each order.

Example:

Food Total: ₦3,000

Delivery Fee: ₦500

Service Fee (5%): ₦150

Total Paid By Student: ₦3,650

Revenue Distribution:

* Restaurant receives ₦3,000
* Rider receives ₦500
* Chowlet receives ₦150

Important:

The 5% service fee is paid by the student and is NOT deducted from restaurant earnings.

---

# Core Features

## Student App

Students can:

* Register and authenticate
* Select their university
* Browse restaurants
* View menus
* Add items to cart
* Checkout
* Pay directly
* Pay using wallet balance
* Track orders in real time
* View order history
* Manage profile and wallet

---

## Restaurant Dashboard

Restaurants can:

* Create and manage menus
* Manage food availability
* Receive incoming orders
* Accept or reject orders
* Update preparation status
* View order history
* Monitor earnings

---

## Rider Dashboard

Riders can:

* View assigned deliveries
* Accept delivery assignments
* Update delivery status
* Mark deliveries completed
* Track earnings

---

## School Administration Dashboard

School administrators can:

* Manage restaurants
* Manage riders
* Manage delivery points
* Monitor orders
* View analytics
* View revenue reports
* Manage payouts

---

# Multi-Tenant Architecture

Chowlet is designed as a multi-tenant platform.

Each university operates as an isolated tenant.

Every core record is associated with a:

* school_id

Examples:

* Users belong to a school
* Restaurants belong to a school
* Riders belong to a school
* Orders belong to a school
* Delivery points belong to a school

This architecture allows multiple universities to use the same platform while keeping data isolated.

---

# Payment System

Chowlet supports two payment methods.

## Direct Payment

Student pays for an order immediately using Paystack.

Flow:

Order → Paystack → Verification → Order Confirmed

---

## Wallet Payment

Student funds wallet using Paystack.

Wallet balance can then be used for future orders.

Flow:

Fund Wallet → Wallet Balance Updated → Checkout Using Wallet

---

# Delivery Model

Deliveries are restricted to locations within school premises.

Instead of arbitrary addresses, the platform uses predefined delivery points.

Examples:

* Hostel A Gate
* Faculty of Science
* Engineering Building
* Main Library
* Student Centre

This approach simplifies logistics and improves delivery efficiency.

---

# User Roles

## Student

* Browse restaurants
* Place orders
* Track deliveries
* Manage wallet

## Restaurant

* Manage menu
* Manage orders

## Rider

* Deliver orders
* Update delivery status

## School Admin

* Manage operations within a school

## Super Admin

* Manage entire platform
* Manage schools
* Access platform-wide analytics

---

# Technology Stack

## Mobile Application

* React Native
* Expo
* TypeScript
* Expo Router
* TanStack Query
* NativeWind

---

## Admin Dashboard

* Next.js
* TypeScript
* Tailwind CSS
* shadcn/ui

---

## Backend

* FastAPI
* Python
* SQLAlchemy 2.0
* Alembic
* Pydantic

---

## Authentication

* Supabase Auth
* JWT Authentication
* Email Verification
* Password Reset

FastAPI verifies Supabase-issued JWT tokens.

---

## Database

* Neon PostgreSQL

Database responsibilities:

* Users
* Restaurants
* Menus
* Orders
* Wallets
* Payments
* Payouts
* Analytics

---

## Storage

* Supabase Storage

Used for:

* Restaurant images
* Menu images
* Verification documents

---

## Payments

* Paystack

Used for:

* Direct payments
* Wallet funding
* Payment verification

---

## Realtime

Initial Version:

* Supabase Realtime

Future Upgrade:

* Redis
* WebSockets

---

## Background Jobs (Future)

* Redis
* Celery

Used for:

* Notifications
* Payment processing
* Automated rider assignment
* Scheduled tasks

---

# MVP Goal

Launch successfully within a single university.

Validate:

* Student demand
* Restaurant adoption
* Delivery operations
* Payment flows

After validation, onboard additional universities without changing the underlying architecture.

---

# Long-Term Vision

To become the leading campus commerce platform in Nigeria by providing:

* Food ordering
* Campus logistics
* Vendor management
* Student wallet services
* Campus marketplace infrastructure

Starting with food delivery and expanding into broader campus services.
