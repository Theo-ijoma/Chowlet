# Chowlet 🍽️

Campus Food Ordering & Delivery Platform

## Overview

Chowlet is a campus-first food ordering and delivery platform built to eliminate long queues in university cafeterias and restaurants.

Students can browse menus, place orders, make payments, and receive food deliveries anywhere within their school campus.

Chowlet is designed specifically for universities and tertiary institutions, allowing multiple schools to operate independently within the same platform.

---

## Problem

Students often experience:

* Long queues at cafeterias
* Delays during peak hours
* Missed lectures due to waiting for food
* No centralized ordering system
* No visibility into restaurant availability

Chowlet solves this by enabling students to order food from their phones and receive deliveries within campus.

---

## Vision

To become the leading campus food commerce platform in Nigeria.

Starting with food delivery and eventually expanding into broader campus services.

---

## Business Model

Chowlet earns revenue through a platform service fee.

Example:

Food Total: ₦5,000

Platform Fee (5%): ₦250

Customer Pays: ₦5,250

Restaurant Receives: ₦5,000

Chowlet Receives: ₦250

The platform fee is added to the customer's total and is not deducted from restaurant earnings.

---

## Core Features

### Student Mobile App

* Sign up and authentication
* Browse restaurants
* Browse menus
* Add items to cart
* Place orders
* Pay online
* Fund wallet
* Pay using wallet balance
* Track order status
* View order history
* Manage profile

### Restaurant Portal

* Manage menu categories
* Manage menu items
* Manage restaurant profile
* Receive orders
* Accept or reject orders
* Update order status
* View sales analytics

### Dispatch Dashboard

* View active deliveries
* Assign riders
* Monitor delivery progress
* Manage delivery operations

### Admin Dashboard

* Manage schools
* Manage restaurants
* Manage users
* Monitor transactions
* View platform analytics
* Manage platform operations

---

## Multi-School Architecture

Each university operates independently.

Example:

University A

* Students
* Restaurants
* Orders
* Delivery Locations

University B

* Students
* Restaurants
* Orders
* Delivery Locations

Data remains isolated per school while running on a shared platform.

---

## Tech Stack

### Mobile App

* React Native
* Expo
* TypeScript
* Expo Router
* TanStack Query
* Zustand

### Admin Dashboard

* Next.js
* TypeScript
* Tailwind CSS
* shadcn/ui

### Backend

* Bun
* Express.js
* TypeScript
* Prisma ORM

### Database

* Neon PostgreSQL

### Authentication

* Supabase Auth

Supabase is used only for:

* Sign Up
* Sign In
* Password Reset
* Email Verification
* Session Management

### Storage

* Cloudinary

Used for:

* Food images
* Restaurant logos
* Restaurant banners
* Profile images

### Payments

* Paystack

Used for:

* Order payments
* Wallet funding
* Transaction verification

### Realtime

* Native WebSockets (ws)

Used for:

* Order status updates
* Restaurant notifications
* Dispatch updates
* Delivery tracking

### Deployment

Backend

* Railway or Fly.io

Admin Dashboard

* Vercel

Database

* Neon

---

## Project Structure

```
chowlet/
│
├── backend/
│   ├── prisma/
│   └── src/
│
├── mobile/
│
├── admin/
│
└── docs/
```

---

## Database Design

### Core Tables

* schools
* profiles
* restaurants
* menu_categories
* menu_items
* delivery_locations
* orders
* order_items
* wallets
* wallet_transactions
* payments

---

## Realtime Flow

Restaurant Accepts Order

↓

Backend Updates Database

↓

WebSocket Event Emitted

↓

Student Receives Instant Update

Example Status Flow:

PENDING

↓

ACCEPTED

↓

PREPARING

↓

READY

↓

OUT_FOR_DELIVERY

↓

DELIVERED

---

## MVP Scope

### Student App

* Authentication
* Browse restaurants
* Browse menu
* Place order
* Online payment
* Order tracking

### Restaurant Dashboard

* Manage menu
* Manage orders
* Update order status

### Admin Dashboard

* Manage schools
* Manage restaurants
* View orders

---

## Development Roadmap

### Phase 1

Foundation

* [x] Project setup
* [x] GitHub repository
* [x] Neon database
* [x] Architecture planning
* [ ] Prisma setup
* [ ] School model
* [ ] Profile model

### Phase 2

Restaurant System

* [ ] Restaurants
* [ ] Menu categories
* [ ] Menu items

### Phase 3

Ordering System

* [ ] Cart
* [ ] Orders
* [ ] Order items

### Phase 4

Payments

* [ ] Paystack integration
* [ ] Wallet funding
* [ ] Wallet payments

### Phase 5

Realtime

* [ ] WebSocket server
* [ ] Order events
* [ ] Delivery updates

### Phase 6

Production Launch

* [ ] Pilot school onboarding
* [ ] Restaurant onboarding
* [ ] Student testing

---

## Current Status

🚧 Active Development

Target: Launch the first MVP in a single university before expanding to multiple campuses across Nigeria.
