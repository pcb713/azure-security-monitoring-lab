# Monitoring Architecture

## Components

Azure Virtual Machines generate logs which are sent to
Azure Monitor and Microsoft Sentinel for analysis.

Security alerts are generated when suspicious activity
is detected.

## Monitoring Flow

Azure Resource → Log Collection → Log Analytics Workspace →
Security Alerts → SOC Investigation
