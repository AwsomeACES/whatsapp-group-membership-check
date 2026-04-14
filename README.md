# whatsapp-group-membership-check

Open-source reference code for the WhatsApp group membership verification used in signup.

## What this code does

This code checks whether a phone number belongs to a selected WhatsApp group.

## What this code does not do

- It does not read group messages
- It does not monitor conversations
- It does not access chat history
- It does not process message content
- It does not collect anything beyond what is needed for membership verification

## Why we are publishing this

We want community admins and users to be able to review the exact logic used in our WhatsApp signup flow.

## How it works

1. The user selects their WhatsApp group
2. The system checks whether their phone number is a member of that group
3. If membership is confirmed, the OTP flow continues
4. If membership is not confirmed, signup is blocked

## Important note

WhatsApp bots or integrations must be explicitly enabled for a group before any automation can work. This code is designed around membership verification only.

## Code walkthrough

We are happy to provide a code walkthrough for community admins who want to review the implementation in more detail.
