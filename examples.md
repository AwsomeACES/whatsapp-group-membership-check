# Example

## Purpose

This example shows the type of participant-list lookup used for membership verification.

## Input

- Phone number: `+1 555 123 4567`
- Group ID: `120363420581199245@g.us`

## Endpoint

`GET /api/group/{group_jid}/participants`

## Result handling

- If the phone number appears in the participants list, membership is confirmed
- If the phone number does not appear, membership is not confirmed
- If the endpoint is unavailable, the system should fail safely and avoid claiming message access

## Privacy note

This verification checks membership only.
It does not read group messages, chat history, or conversation content.
